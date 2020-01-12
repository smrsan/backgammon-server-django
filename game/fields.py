from django.db import models

from .utils import get_rand_str


class RandomStrField(models.CharField):

    description = "A CharField with a generated random string value."

    def __init__(self, *args, **kwargs):
        kwargs['default'] = get_rand_str(length=kwargs.get('max_length', 24))
        super().__init__(*args, **kwargs)
