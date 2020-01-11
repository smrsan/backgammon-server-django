from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    started = models.DateTimeField(null=True)

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
    is_owner_home_right = models.BooleanField(default=True)


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
    black_bead_01_position = models.IntegerField(default=6)
    black_bead_02_position = models.IntegerField(default=6)
    black_bead_03_position = models.IntegerField(default=6)
    black_bead_04_position = models.IntegerField(default=6)
    black_bead_05_position = models.IntegerField(default=6)
    black_bead_06_position = models.IntegerField(default=8)
    black_bead_07_position = models.IntegerField(default=8)
    black_bead_08_position = models.IntegerField(default=8)
    black_bead_09_position = models.IntegerField(default=13)
    black_bead_10_position = models.IntegerField(default=13)
    black_bead_11_position = models.IntegerField(default=13)
    black_bead_12_position = models.IntegerField(default=13)
    black_bead_13_position = models.IntegerField(default=13)
    black_bead_14_position = models.IntegerField(default=24)
    black_bead_15_position = models.IntegerField(default=24)

    white_bead_01_position = models.IntegerField(default=19)
    white_bead_02_position = models.IntegerField(default=19)
    white_bead_03_position = models.IntegerField(default=19)
    white_bead_04_position = models.IntegerField(default=19)
    white_bead_05_position = models.IntegerField(default=19)
    white_bead_06_position = models.IntegerField(default=17)
    white_bead_07_position = models.IntegerField(default=17)
    white_bead_08_position = models.IntegerField(default=17)
    white_bead_09_position = models.IntegerField(default=12)
    white_bead_10_position = models.IntegerField(default=12)
    white_bead_11_position = models.IntegerField(default=12)
    white_bead_12_position = models.IntegerField(default=12)
    white_bead_13_position = models.IntegerField(default=12)
    white_bead_14_position = models.IntegerField(default=1)
    white_bead_15_position = models.IntegerField(default=1)


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
