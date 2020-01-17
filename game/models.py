from django.db import models
from django.contrib.auth.models import User

from jsonfield import JSONField

from .fields import RandomStrField
from .constants import black_home_start


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    started = models.DateTimeField(null=True)

    ended = models.DateTimeField(null=True)

    private = models.BooleanField(default=False)

    invite_token = RandomStrField(max_length=24)

    # Player1 = owner
    owner = models.ForeignKey(
        'auth.User',
        related_name='owned_games',
        on_delete=models.CASCADE
    )

    # Player2 Opponent
    opponent = models.ForeignKey(
        'auth.User',
        related_name='attended_games',
        on_delete=models.SET_NULL,
        null=True
    )

    winner = models.ForeignKey(
        'auth.User',
        related_name='won_games',
        on_delete=models.SET_NULL,
        null=True
    )

    is_owner_black = models.BooleanField(default=True)
    is_owner_home_start = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']


class Board(models.Model):
    game = models.OneToOneField(
        Game,
        primary_key=True,
        related_name='board',
        on_delete=models.CASCADE,
    )

    # Position Meanings:
    # 0 -> Hitted
    # 1-24 -> On Board
    # 25 -> Beared Off
    beads = JSONField(default=black_home_start)


class Turn(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(null=True)

    game = models.ForeignKey(
        Game,
        related_name='turns',
        on_delete=models.CASCADE,
    )

    player = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True
    )

    first_dice = models.IntegerField(null=True)
    second_dice = models.IntegerField(null=True)

    first_move = models.IntegerField(null=True)
    second_move = models.IntegerField(null=True)

    next_turn = models.ForeignKey(
        'Turn',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ['started']
