import json
import logging
import statistics
from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.http import (Http404, HttpRequest, HttpResponse,
                         HttpResponseBadRequest, JsonResponse)
from django.shortcuts import render
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

LOGGER = logging.getLogger(__name__)


def get_weather_details(request: HttpRequest, city: str) -> JsonResponse:
    """Validate api request and return city weather information.

    Fetch weather from a public api and compute min,max,average,and median temperature.

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
    # import pdb;pdb.set_trace()
    from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    to_date = datetime.now().strftime("%Y-%m-%d")
    url = f"http://api.weatherapi.com/v1/history.json?key={settings.WEATHER_API_KEY}&q={city}&dt={from_date}&end_dt={to_date}"
    response = requests.get(url=url)
    daily_temepratues = [
        response.json()
        .get("forecast")
        .get("forecastday")[i]
        .get("day")
        .get("avgtemp_c")
        for i in range(days)
    ]
    max_temperature = max(daily_temepratues)
    min_temperature = min(daily_temepratues)
    average_temperature = statistics.mean(daily_temepratues)
    median_temperature = statistics.median(daily_temepratues)

    return JsonResponse(
        {
            # "daily_temps": daily_temepratues,
            "maximum": max_temperature,
            "minimum": min_temperature,
            "average": average_temperature,
            "median": median_temperature,
            # "days" : days,
        },
        status=200,
    )
