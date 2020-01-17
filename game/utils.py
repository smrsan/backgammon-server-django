from random import choice
from string import ascii_letters, digits
from django.db.models import Q

from .models import Game


def get_rand_str(length=12):
    return ''.join(choice(ascii_letters + digits) for _ in range(length))


def has_game(user_id):
    return bool(Game.objects.get(
        Q(owner=user_id) | Q(opponent=user_id),
        Q(ended=None)
    ))
