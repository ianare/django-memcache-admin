
from __future__ import unicode_literals

from django.shortcuts import redirect, render_to_response
from django.contrib import messages
from django.contrib.admin import site
from django.template import RequestContext
from django.core.cache import cache, get_cache
from django.conf import settings
from django.utils.translation import ugettext as _

if get_cache.__module__.startswith('debug_toolbar'):
    from debug_toolbar.panels.cache import base_get_cache as get_cache

SETTINGS = {
    'REFRESH_RATE': 5000,
    'CACHE': 'default',
}
if hasattr(settings, 'MEMCACHE_ADMIN'):
    SETTINGS = dict(SETTINGS.items() + settings.MEMCACHE_ADMIN.items())

mc_client = get_cache(SETTINGS['CACHE'])._cache


def _percent(data, part, total):
    """
    Calculate a percentage.
    """
    try:
        return round(100 * float(data[part]) / float(data[total]), 1)
    except ZeroDivisionError:
        return 0


def _get_cache_stats(server_name=None):
    """
    Get stats info.
    """
    server_info = {}
    for svr in mc_client.get_stats():
        svr_info = svr[0].split(' ')
        svr_name = svr_info[0]
        svr_stats = svr[1]
        svr_stats['bytes_percent'] = _percent(svr_stats, 'bytes', 'limit_maxbytes')
        svr_stats['get_hit_rate'] = _percent(svr_stats, 'get_hits', 'cmd_get')
        svr_stats['get_miss_rate'] = _percent(svr_stats, 'get_misses', 'cmd_get')
        if server_name and server_name == svr_name:
            return svr_stats
        server_info[svr_name] = svr_stats
    return server_info


def _get_cache_slabs(server_name=None):
    """
    Get slabs info.
    """
    server_info = {}
    for svr in mc_client.get_slabs():
        svr_info = svr[0].split(' ')
        svr_name = svr_info[0]
        if server_name and server_name == svr_name:
            return svr[1]
        server_info[svr_name] = svr[1]
    return server_info


def _context_data(data):
    """
    Add admin global context, for compatibility with Django 1.7
    """
    try:
        return dict(site.each_context().items() + data.items())
    except AttributeError:
        return data


def server_status(request):
    """
    Return the status of all servers.
    """
    data = {
        'cache_stats': _get_cache_stats(),
        'can_get_slabs': hasattr(mc_client, 'get_slabs'),
    }
    return render_to_response('memcache_admin/server_status.html', data, RequestContext(request))


def dashboard(request):
    """
    Show the dashboard.
    """
    cache_stats = _get_cache_stats()
    if cache_stats:
        data = _context_data({
            'title': _('Memcache Dashboard'),
            'cache_stats': cache_stats,
            'can_get_slabs': hasattr(mc_client, 'get_slabs'),
            'REFRESH_RATE': SETTINGS['REFRESH_RATE'],
        })
        template = 'memcache_admin/dashboard.html'
    else:
        data = _context_data({
            'title': _('Memcache Dashboard - Error'),
            'error_message': _('Unable to connect to a memcache server.'),
        })
        template = 'memcache_admin/dashboard_error.html'
    return render_to_response(template, data, RequestContext(request))


def stats(request, server_name):
    """
    Show server statistics.
    """
    server_name = server_name.strip('/')
    data = _context_data({
        'title': _('Memcache Statistics for %s') % server_name,
        'cache_stats': _get_cache_stats(server_name),
    })
    return render_to_response('memcache_admin/stats.html', data, RequestContext(request))


def slabs(request, server_name):
    """
    Show server slabs.
    """
    data = _context_data({
        'title': _('Memcache Slabs for %s') % server_name,
        'cache_slabs': _get_cache_slabs(server_name),
    })
    return render_to_response('memcache_admin/slabs.html', data, RequestContext(request))


def flush(request):
    """
    Flush servers.
    """
    cache.clear()
    messages.success(request, _('Memcache was flushed.'))
    return redirect('admin:mc_dashboard')
