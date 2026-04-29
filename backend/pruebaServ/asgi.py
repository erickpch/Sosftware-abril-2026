"""
ASGI config for pruebaServ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import  AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import pruebaServ.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pruebaServ.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(pruebaServ.routing.websocket_urlpatterns)
    )
})
