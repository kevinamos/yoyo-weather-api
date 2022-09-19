from django.conf import settings as django_settings
from django.urls import path

from weather_calculator.api import get_weather_details_api

urlpatterns = [
    path(r"api/locations/<str:city>/", get_weather_details_api),
]
