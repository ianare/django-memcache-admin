
from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('memcache_admin.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^flush/$', 'flush', name='flush'),
    url(r'^stats/(?P<server_name>.+)$', 'stats', name='stats'),
    url(r'^slabs/(?P<server_name>.+)$', 'slabs', name='slabs'),
)
