
from __future__ import unicode_literals

from django.test import TestCase
from django.core.cache import cache


def _random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))


# This should fill a 64MB server to 96%
for i in range(1000):
    cache.set(_random_string(11), _random_string(64350))
