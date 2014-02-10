from __future__ import unicode_literals

from django.contrib import admin
from django.conf.urls import patterns, url

from .models import Dashboard
from . import views


class MemcachedAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def get_urls(self):
        urls = super(MemcachedAdmin, self).get_urls()
        urlpatterns = patterns(
            'memcache_admin.views',
            url(r'^$', self.admin_site.admin_view(views.dashboard), name='mc_dashboard'),
            url(r'^flush/$', self.admin_site.admin_view(views.flush), name='mc_flush'),
            url(r'^stats/(?P<server_name>.+)$', self.admin_site.admin_view(views.stats), name='mc_stats'),
            url(r'^slabs/(?P<server_name>.+)$', self.admin_site.admin_view(views.slabs), name='mc_slabs'),
            url(r'^server_status/$', self.admin_site.admin_view(views.server_status), name='mc_server_status'),
        )
        return urlpatterns + urls


admin.site.register(Dashboard, MemcachedAdmin)