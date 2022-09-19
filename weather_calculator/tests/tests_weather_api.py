from unittest.mock import patch

from django.test import RequestFactory, TestCase
from rest_framework.test import APIRequestFactory

from weather_calculator.api import get_weather_details_api

# Create your tests here.


class TestGetWeatherDetailsAPI(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        """Test ton check if api calls function correctly and return no errors.

        Consider monkeypatching this in future to avoid direct api calls, then test
        the max, min, mean and median calculations.
        """
        api_factory = APIRequestFactory()
        request = api_factory.get("api/locations/Nairobi/?days=10")
        response = get_weather_details_api(request, city="Nairobi")
        assert response.status_code == 200
        # Test with Non existent city
        response = get_weather_details_api(request, city="NaiZHSDJHIUDSHFIKDFJH")
        assert response.status_code == 400
        # Test with a negative number of days
        request = api_factory.get("api/locations/Nairobi/?days=-9")
        response = get_weather_details_api(request, city="London")
        assert response.status_code == 400
        # Test with a really large number of days
        request = api_factory.get("api/locations/Nairobi/?days=999")
        response = get_weather_details_api(request, city="London")
        assert response.status_code == 400
        import pdb

        pdb.set_trace()


# class MockResponse:

#     def __init__(self):
#         self.status_code = 200

#     def json(self):
#         return {
#         {
#     "location": {
#         "name": "Nairobi",
#         "region": "Nairobi Area",
#         "country": "Kenya",
#         "lat": -1.28,
#         "lon": 36.82,
#         "tz_id": "Africa/Nairobi",
#         "localtime_epoch": 1663564651,
#         "localtime": "2022-09-19 8:17"
#     },
#     "forecast": {
#         "forecastday": [
#             {
#                 "date": "2022-09-17",
#                 "date_epoch": 1663372800,
#                 "day": {
#                     "maxtemp_c": 29.3,
#                     "maxtemp_f": 84.7,
#                     "mintemp_c": 15.1,
#                     "mintemp_f": 59.2,
#                     "avgtemp_c": 22.1,
#                     "avgtemp_f": 71.7,
#                     "maxwind_mph": 15.0,
#                     "maxwind_kph": 24.1,
#                     "totalprecip_mm": 0.0,
#                     "totalprecip_in": 0.0,
#                     "avgvis_km": 10.0,
#                     "avgvis_miles": 6.0,
#                     "avghumidity": 60.0,
#                     "condition": {
#                         "text": "Partly cloudy",
#                         "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#                         "code": 1003
#                     },
#                     "uv": 0.0
#                 },
#                 "astro": {
#                     "sunrise": "06:24 AM",
#                     "sunset": "06:30 PM",
#                     "moonrise": "No moonrise",
#                     "moonset": "11:53 AM",
#                     "moon_phase": "Waning Gibbous",
#                     "moon_illumination": "56"
#                 },
#                 "hour": [
#                     {
#                         "time_epoch": 1663362000,
#                         "time": "2022-09-17 00:00",
#                         "temp_c": 15.6,
#                         "temp_f": 60.1,
#                         "is_day": 0,
#                         "condition": {
#                             "text": "Cloudy",
#                             "icon": "//cdn.weatherapi.com/weather/64x64/night/119.png",
#                             "code": 1006
#                         },
#                         "wind_mph": 8.1,
#                         "wind_kph": 13.0,
#                         "wind_degree": 81,
#                         "wind_dir": "E",
#                         "pressure_mb": 1018.0,
#                         "pressure_in": 30.05,
#                         "precip_mm": 0.0,
#                         "precip_in": 0.0,
#                         "humidity": 80,
#                         "cloud": 70,
#                         "feelslike_c": 15.6,
#                         "feelslike_f": 60.1,
#                         "windchill_c": 15.6,
#                         "windchill_f": 60.1,
#                         "heatindex_c": 15.6,
#                         "heatindex_f": 60.1,
#                         "dewpoint_c": 12.2,
#                         "dewpoint_f": 54.0,
#                         "will_it_rain": 0,
#                         "chance_of_rain": 0,
#                         "will_it_snow": 0,
#                         "chance_of_snow": 0,
#                         "vis_km": 10.0,
#                         "vis_miles": 6.0,
#                         "gust_mph": 10.3,
#                         "gust_kph": 16.6
#                     },
#                     {
#                         "time_epoch": 1663444800,
#                         "time": "2022-09-17 23:00",
#                         "temp_c": 16.6,
#                         "temp_f": 61.9,
#                         "is_day": 0,
#                         "condition": {
#                             "text": "Partly cloudy",
#                             "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
#                             "code": 1003
#                         },
#                         "wind_mph": 10.1,
#                         "wind_kph": 16.2,
#                         "wind_degree": 84,
#                         "wind_dir": "E",
#                         "pressure_mb": 1016.0,
#                         "pressure_in": 30.0,
#                         "precip_mm": 0.0,
#                         "precip_in": 0.0,
#                         "humidity": 73,
#                         "cloud": 28,
#                         "feelslike_c": 16.6,
#                         "feelslike_f": 61.9,
#                         "windchill_c": 16.6,
#                         "windchill_f": 61.9,
#                         "heatindex_c": 16.6,
#                         "heatindex_f": 61.9,
#                         "dewpoint_c": 11.7,
#                         "dewpoint_f": 53.0,
#                         "will_it_rain": 0,
#                         "chance_of_rain": 1,
#                         "will_it_snow": 0,
#                         "chance_of_snow": 0,
#                         "vis_km": 10.0,
#                         "vis_miles": 6.0,
#                         "gust_mph": 12.3,
#                         "gust_kph": 19.8
#                     }
#                 ]
#             },
#             {
#                 "date": "2022-09-18",
#                 "date_epoch": 1663459200,
#                 "day": {
#                     "maxtemp_c": 27.5,
#                     "maxtemp_f": 81.5,
#                     "mintemp_c": 13.9,
#                     "mintemp_f": 57.0,
#                     "avgtemp_c": 21.4,
#                     "avgtemp_f": 70.6,
#                     "maxwind_mph": 13.2,
#                     "maxwind_kph": 21.2,
#                     "totalprecip_mm": 0.0,
#                     "totalprecip_in": 0.0,
#                     "avgvis_km": 10.0,
#                     "avgvis_miles": 6.0,
#                     "avghumidity": 61.0,
#                     "condition": {
#                         "text": "Partly cloudy",
#                         "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#                         "code": 1003
#                     },
#                     "uv": 0.0
#                 },
#                 "astro": {
#                     "sunrise": "06:24 AM",
#                     "sunset": "06:30 PM",
#                     "moonrise": "12:25 AM",
#                     "moonset": "12:44 PM",
#                     "moon_phase": "Third Quarter",
#                     "moon_illumination": "50"
#                 },
#                 "hour": [
#                     {
#                         "time_epoch": 1663448400,
#                         "time": "2022-09-18 00:00",
#                         "temp_c": 15.7,
#                         "temp_f": 60.3,
#                         "is_day": 0,
#                         "condition": {
#                             "text": "Partly cloudy",
#                             "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
#                             "code": 1003
#                         },
#                         "wind_mph": 7.6,
#                         "wind_kph": 12.2,
#                         "wind_degree": 75,
#                         "wind_dir": "ENE",
#                         "pressure_mb": 1017.0,
#                         "pressure_in": 30.02,
#                         "precip_mm": 0.0,
#                         "precip_in": 0.0,
#                         "humidity": 76,
#                         "cloud": 33,
#                         "feelslike_c": 15.7,
#                         "feelslike_f": 60.3,
#                         "windchill_c": 15.7,
#                         "windchill_f": 60.3,
#                         "heatindex_c": 15.7,
#                         "heatindex_f": 60.3,
#                         "dewpoint_c": 11.5,
#                         "dewpoint_f": 52.7,
#                         "will_it_rain": 0,
#                         "chance_of_rain": 0,
#                         "will_it_snow": 0,
#                         "chance_of_snow": 0,
#                         "vis_km": 10.0,
#                         "vis_miles": 6.0,
#                         "gust_mph": 9.8,
#                         "gust_kph": 15.8
#                     }

#                 ]
#             },
#             {
#                 "date": "2022-09-19",
#                 "date_epoch": 1663545600,
#                 "day": {
#                     "maxtemp_c": 28.0,
#                     "maxtemp_f": 82.4,
#                     "mintemp_c": 14.2,
#                     "mintemp_f": 57.6,
#                     "avgtemp_c": 22.0,
#                     "avgtemp_f": 71.5,
#                     "maxwind_mph": 13.6,
#                     "maxwind_kph": 22.0,
#                     "totalprecip_mm": 0.2,
#                     "totalprecip_in": 0.01,
#                     "avgvis_km": 10.0,
#                     "avgvis_miles": 6.0,
#                     "avghumidity": 59.0,
#                     "condition": {
#                         "text": "Patchy rain possible",
#                         "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
#                         "code": 1063
#                     },
#                     "uv": 0.0
#                 },
#                 "astro": {
#                     "sunrise": "06:23 AM",
#                     "sunset": "06:29 PM",
#                     "moonrise": "01:16 AM",
#                     "moonset": "01:35 PM",
#                     "moon_phase": "Third Quarter",
#                     "moon_illumination": "43"
#                 },
#                 "hour": [
#                     {
#                         "time_epoch": 1663534800,
#                         "time": "2022-09-19 00:00",
#                         "temp_c": 17.0,
#                         "temp_f": 62.6,
#                         "is_day": 0,
#                         "condition": {
#                             "text": "Partly cloudy",
#                             "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
#                             "code": 1003
#                         },
#                         "wind_mph": 9.2,
#                         "wind_kph": 14.8,
#                         "wind_degree": 84,
#                         "wind_dir": "E",
#                         "pressure_mb": 1017.0,
#                         "pressure_in": 30.02,
#                         "precip_mm": 0.0,
#                         "precip_in": 0.0,
#                         "humidity": 71,
#                         "cloud": 28,
#                         "feelslike_c": 17.0,
#                         "feelslike_f": 62.6,
#                         "windchill_c": 17.0,
#                         "windchill_f": 62.6,
#                         "heatindex_c": 17.0,
#                         "heatindex_f": 62.6,
#                         "dewpoint_c": 11.7,
#                         "dewpoint_f": 53.1,
#                         "will_it_rain": 0,
#                         "chance_of_rain": 0,
#                         "will_it_snow": 0,
#                         "chance_of_snow": 0,
#                         "vis_km": 10.0,
#                         "vis_miles": 6.0,
#                         "gust_mph": 11.4,
#                         "gust_kph": 18.4
#                     },
#                     {
#                         "time_epoch": 1663588800,
#                         "time": "2022-09-19 15:00",
#                         "temp_c": 28.0,
#                         "temp_f": 82.4,
#                         "is_day": 1,
#                         "condition": {
#                             "text": "Partly cloudy",
#                             "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#                             "code": 1003
#                         },
#                         "wind_mph": 10.3,
#                         "wind_kph": 16.6,
#                         "wind_degree": 85,
#                         "wind_dir": "E",
#                         "pressure_mb": 1009.0,
#                         "pressure_in": 29.81,
#                         "precip_mm": 0.0,
#                         "precip_in": 0.0,
#                         "humidity": 29,
#                         "cloud": 27,
#                         "feelslike_c": 26.9,
#                         "feelslike_f": 80.4,
#                         "windchill_c": 28.0,
#                         "windchill_f": 82.4,
#                         "heatindex_c": 26.9,
#                         "heatindex_f": 80.4,
#                         "dewpoint_c": 8.4,
#                         "dewpoint_f": 47.1,
#                         "will_it_rain": 0,
#                         "chance_of_rain": 0,
#                         "will_it_snow": 0,
#                         "chance_of_snow": 0,
#                         "vis_km": 10.0,
#                         "vis_miles": 6.0,
#                         "gust_mph": 11.9,
#                         "gust_kph": 19.1
#                     }
#                 ]
#             }
#         ]
#     }
# }
#         }
# request = factory.get("api/locations/Nairobi/?days=10", content_type="application/json")
