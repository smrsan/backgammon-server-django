from django.db.models import Q

from .models import Game


def has_game(user_id):
    return bool(Game.objects.get(
        Q(owner=user_id) | Q(opponent=user_id),
        Q(ended=None)
    ))
