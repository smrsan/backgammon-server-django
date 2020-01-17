from django.urls import re_path

from .consumers import GameConsumer, ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/game/(?P<room_name>\w+)/$', GameConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]
