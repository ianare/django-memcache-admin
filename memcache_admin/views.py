
from __future__ import unicode_literals

from django.shortcuts import redirect, render_to_response
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext
from django.core.cache import cache

mc_client = cache._cache

def _percent(data, part, total):
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


def dashboard(request):
    """
    Show the dashboard.
    """
    data = {
        'title': 'Memcache Dashboard',
        'cache_stats': _get_cache_stats(),
        'can_get_slabs': hasattr(mc_client, 'get_slabs')
    }
    return render_to_response('memcache_admin/dashboard.html', data, RequestContext(request))


def stats(request, server_name):
    """
    Show server tatistics.
    """
    server_name = server_name.strip('/')
    data = {
        'title': 'Memcache Statistics for %s' % server_name,
        'cache_stats': _get_cache_stats(server_name)
    }
    return render_to_response('memcache_admin/stats.html', data, RequestContext(request))


def slabs(request, server_name):
    """
    Show server slabs.
    """
    data = {
        'title': 'Memcache Slabs for %s' % server_name,
        'cache_slabs': _get_cache_slabs(server_name)
    }
    return render_to_response('memcache_admin/slabs.html', data, RequestContext(request))


def flush(request):
    """
    Flush servers.
    """
    cache.clear()
    messages.success(request, 'Memcache was flushed.')
    return redirect('admin:mc_dashboard')
