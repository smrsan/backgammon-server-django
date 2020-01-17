from random import choice
from string import ascii_letters, digits
from django.db.models import Q


def get_rand_str(length=12):
    return ''.join(choice(ascii_letters + digits) for _ in range(length))
