from django.urls import path
from visita.views import VideoStreamingConsumer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path

urlpatterns = [
    # Tus rutas van aquí
]

websocket_urlpatterns = [
    path('ws/video_stream/', VideoStreamingConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
