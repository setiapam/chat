from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from chat import Consumer

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/(?P<person_name>\w+)/$', Consumer.Consumer)
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
