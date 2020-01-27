from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from .channelsmiddleware import TokenAuthMiddleware
from game import routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            TokenAuthMiddleware(
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        )
    )
})
