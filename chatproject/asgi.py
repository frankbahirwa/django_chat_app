import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from chats.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("ws/chat/<str:username>/", ChatConsumer.as_asgi()),
            ])
        ),
    ),
})
