from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, GameViewSet, BoardViewSet, TurnViewSet


router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet)
router_v1.register(r'games', GameViewSet)
router_v1.register(r'boards', BoardViewSet)
router_v1.register(r'turns', TurnViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
