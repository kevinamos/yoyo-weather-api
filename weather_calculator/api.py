import logging
import statistics
from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from rest_framework import status

LOGGER = logging.getLogger(__name__)


def get_weather_details_api(request: HttpRequest, city: str) -> JsonResponse:
    """Validate api request and return city weather information.

    Fetch weather from a public api and compute min,max,average,and median temperature.
    Currently API fetches historical records but can be modified to fetch forecast data.

    Args:
        request (HttpRequest):
            request containing number of days.
        city (str):
            The city which we want to get weather information.

    Returns:
        JsonResponse:
            Return the weather details of the city.
            If an error occurs, its returned instead.
    """
    try:
        days = int(request.GET["days"])
    except ValueError:
        return JsonResponse(
            data={
                "success": False,
                "error": True,
                "error_message": "You entered an unsupported number of days:",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    # trial version will get hist
    if days <= 0 or days > 30:

        return JsonResponse(
            data={
                "success": False,
                "error": True,
                "error_message": "You entered an unsupported number of days:",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    to_date = datetime.now().strftime("%Y-%m-%d")
    url = f"http://api.weatherapi.com/v1/history.json?key={settings.WEATHER_API_KEY}&q=\
        {city}&dt={from_date}&end_dt={to_date}"
    response = requests.get(url=url).json()
    if response.get("error"):
        LOGGER.error(
            "Weather API request failed",
            extra={
                "request_headers": request.META,
                "error_message": response.get("error").get("message"),
            },
        )
        return JsonResponse(
            data={
                "success": False,
                "error": True,
                "error_message": response.get("error").get("message"),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    # extract the daily average temperatures for all days requested. Use try to catch
    # any unforeseable api changes from the vendor
    try:
        daily_temepratues = [
            response.get("forecast").get("forecastday")[i].get("day").get("avgtemp_c")
            for i in range(days)
        ]
    except (AttributeError, KeyError, ValueError):
        LOGGER.error(
            "An unknown response from the Weather API",
            extra={
                "request_headers": request.META,
                "api_response_data": response,
            },
        )
        return JsonResponse(
            data={
                "success": False,
                "error": True,
                "error_message": "An unknown occurred during the API call",
            },
            status=status.status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    max_temperature = max(daily_temepratues)
    min_temperature = min(daily_temepratues)
    average_temperature = statistics.mean(daily_temepratues)
    median_temperature = statistics.median(daily_temepratues)

    return JsonResponse(
        data={
            "success": True,
            "error": False,
            "maximum": max_temperature,
            "minimum": min_temperature,
            "average": round(float(average_temperature), 2),
            "median": median_temperature,
        },
        status=200,
    )
