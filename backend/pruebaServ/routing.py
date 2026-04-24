
from django.urls import re_path
from .Consumer import Consumer

websocket_urlpatterns = [
    re_path(r"ws/prueba/",Consumer.as_asgi())
]