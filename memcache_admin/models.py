
from __future__ import unicode_literals

from django.db import models


class Memcached(models.Model):
    class Meta:
        managed = False