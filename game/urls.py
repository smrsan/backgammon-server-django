from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import UserViewSet, GameViewSet, BoardViewSet, TurnViewSet


router_v1 = SimpleRouter()
router_v1.register(r'users', UserViewSet)
router_v1.register(r'games', GameViewSet)

games_router_v1 = NestedSimpleRouter(router_v1, r'games', lookup='game')
games_router_v1.register(r'board', BoardViewSet)
games_router_v1.register(r'turns', TurnViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
