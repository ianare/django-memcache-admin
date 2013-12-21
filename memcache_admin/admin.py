
from __future__ import unicode_literals

from django.contrib import admin
from .models import Memcached
from .urls import urlpatterns


class MemcachedAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_urls(self):
        urls = super(MemcachedAdmin, self).get_urls()
        return urlpatterns + urls


admin.site.register(Memcached, MemcachedAdmin)