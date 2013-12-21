
from __future__ import unicode_literals

from django.shortcuts import redirect, render_to_response
from django.conf import settings
from django.contrib import messages
from django.core.cache import cache


def _get_server_info(info, server_name=None):
    """
    Get slab or stats info by server.
    """
    server_info = {}
    for svr in info:
        svr_info = svr[0].split(' ')
        svr_name = svr_info[0]
        if server_name and server_name == svr_name:
            return svr[1]
        server_info[svr_name] = svr[1]
    return server_info


def _get_cache_stats(server_name=None):
    return _get_server_info(cache._cache.get_stats(), server_name)


def _get_cache_slabs(server_name=None):
    return _get_server_info(cache._cache.get_slabs(), server_name)


def dashboard(request):
    """
    Show the dashboard.
    """
    data = {
        'title': 'Memcache Dashboard',
        'cache_stats': _get_cache_stats()
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
    Flush.
    """
    cache.clear()
    messages.success(request, 'Memcache was flushed.')
    return redirect('/admin/memcache_admin/memcached/')
