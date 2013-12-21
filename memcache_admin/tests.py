
from __future__ import unicode_literals

from django.core.cache import cache
from django.test import TestCase


def _random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))


for i in range(5):
    cache.set(_random_string(10), _random_string(100000))