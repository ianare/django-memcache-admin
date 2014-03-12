
from __future__ import unicode_literals

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'memcache administration commands'
    args = 'flush'
    
    def flush(self, options):
        cache.clear()
        self.stdout.write('Memcache was flushed.')

    def handle(self, *args, **options):
        if len(args) == 1:
            try:
                getattr(self, args[0])(options)
            except AttributeError:
                raise CommandError('Invalid command specified.')
        elif len(args) == 0:
            raise CommandError('A command must be specified.')
        else:
            raise CommandError('Only one command may be specified.')