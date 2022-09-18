from django.conf import settings as django_settings
from django.urls import include, path
from weather_calculator.api import (get_weather_details
)

urlpatterns = [
    path(
        r"api/locations/<str:city>/",get_weather_details
        # WeatherDataCalculator.as_view(),
    ),
]
