from django.contrib.auth.models import User

from rest_framework import serializers, exceptions

from .models import Game, Board, Turn
from .constants import black_home_end


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


class GameSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='id')
    created = serializers.ReadOnlyField(source='created')
    started = serializers.ReadOnlyField(source='started')
    ended = serializers.ReadOnlyField(source='ended')
    invite_token = serializers.ReadOnlyField(source='invite_token')
    owner = serializers.ReadOnlyField(source='owner.username')
    opponent = serializers.ReadOnlyField(source='opponent.username')
    winner = serializers.ReadOnlyField(source='winner.username')

    class Meta:
        model = Game
        fields = [
            'id',
            'created',
            'started',
            'ended',
            'private',
            'invite_token',
            'owner',
            'opponent',
            'winner',
            'is_owner_black',
            'is_owner_home_start'
        ]

    def create(self, validated_data):
        created_game = Game.objects.get(
            owner=self.context['request'].user.id, ended=None)

        if created_game:
            raise exceptions.status.HTTP_400_BAD_REQUEST

        game = Game.objects.create(**validated_data)

        is_owner_black = validated_data.get('is_owner_black', True)
        is_owner_home_start = validated_data.get('is_owner_home_start', True)

        if is_owner_black and not is_owner_home_start or \
                not is_owner_black and is_owner_home_start:
            Board.objects.create(game=game, **black_home_end)
        else:
            Board.objects.create(game=game)

        return game
