# from typing import Any, Dict

# from django.db import models


# class WeatherDataRequests(models.Model):
#     """
#     Saves Weather data.

#     Contains data api requests on weather of various locations/cities.
#     """

#     City = models.CharField(max_length=255)
#     ip_address = models.CharField(max_length=255)
#     created_at = models.DateTimeField()

#     def __str__(self):
#         return f"WeatherDataRequests id {self.id} - {self.ip_address} for {self.city}"

#     @property
#     def base_logging_attributes(self) -> Dict[str, Dict[str, Any]]:
#         """Return the dictionary representation with base attributes for logging.

#         Returns:
#             Dict[str, Dict[str, Any]]:
#                 Dictionary representation with base attributes for logging.
#         """
#         return {
#             "WeatherDataRequests": {
#                 "id": self.id,
#                 "ip": self.ip_address,
#                 "created_at": self.created_at,
#             }
#         }
