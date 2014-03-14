
from __future__ import unicode_literals

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Invalidates all existing memcache items, so that occupied memory will be overwritten by new items."
    
    def flush(self, options):
        cache.clear()
        self.stdout.write('Memcache was flushed.')

    def handle(self, *args, **options):
        if len(args) != 0:
            raise CommandError('No arguments may be specified to this command.')
        else:
            self.flush(options)