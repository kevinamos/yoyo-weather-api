import json
import logging
import statistics
from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

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
    days = int(request.GET["days"])
    # trial version will get hist
    if days < 0 or days > 30:

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
    # wrap in a try except?
    url = f"http://api.weatherapi.com/v1/history.json?key={settings.WEATHER_API_KEY}&q=\
        {city}&dt={from_date}&end_dt={to_date}"
    response = requests.get(url=url).json()
    if response.get("error"):
        return JsonResponse(
            data={
                "success": False,
                "error": True,
                "error_message": response.get("error").get("message"),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    # extract the daily average temperatures for all days requested
    daily_temepratues = [
        response.get("forecast").get("forecastday")[i].get("day").get("avgtemp_c")
        for i in range(days)
    ]
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
