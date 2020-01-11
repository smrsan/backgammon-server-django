from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .models import Game, Board, Turn
from .serializers import UserSerializer, GameSerializer, BoardSerializer, TurnSerializer
from .permissions import HasAccessToGame, HasAccessToGameRelatedModels


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, HasAccessToGame]


class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated, HasAccessToGameRelatedModels]


class TurnViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
    permission_classes = [IsAuthenticated, HasAccessToGameRelatedModels]
