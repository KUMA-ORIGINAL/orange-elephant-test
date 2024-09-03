from django.urls import path
from .consumers import UserConsumer, OrderConsumer

websocket_urlpatterns = [
    path('ws/users/', UserConsumer.as_asgi()),
    path('ws/orders/', OrderConsumer.as_asgi()),
]