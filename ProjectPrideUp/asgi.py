"""
ASGI config for ProjectPrideUp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(  #only allowed hosts will be allowed to open websocket connection
        AuthMiddlewareStack(  #it allows us to get user instance in our consumer code as self.scope["user"]
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    )
})
