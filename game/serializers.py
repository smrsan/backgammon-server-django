from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Game, Board, Turn


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'owned_games',
            'attended_games',
            'won_games'
        ]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'created',
            'started',
            'owner',
            'opponent',
            'winner',
            'is_owner_black',
            'is_owner_home_right',
            'board',
            'turns'
        ]


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = [
            'id',
            'started',
            'ended',
            'game',
            'player',
            'first_dice',
            'second_dice',
            'first_move',
            'second_move',
            'next_turn'
        ]
