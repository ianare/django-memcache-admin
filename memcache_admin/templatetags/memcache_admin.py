
from __future__ import unicode_literals

from django import template
from datetime import timedelta, datetime


register = template.Library()


@register.filter
def human_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2f GB' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2f MB' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2f KB' % kilobytes
    else:
        size = '%.2f B' % bytes
    return size


@register.filter
def timestamp(value):
    return timedelta(0, int(value))


@register.filter
def datetimestamp(value):
    return datetime.fromtimestamp(int(value)).strftime('%x %X')


@register.filter
def yes_no(value):
    if int(value):
        return 'Yes'
    else:
        return 'No'
