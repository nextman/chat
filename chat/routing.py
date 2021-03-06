from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chatroom.consumers import ChatConsumer


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("^chat/$", ChatConsumer),
        ])
    ),
})