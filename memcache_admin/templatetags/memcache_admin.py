
from __future__ import unicode_literals

from django import template
from django.utils.translation import ugettext as _
from datetime import timedelta, datetime


register = template.Library()


@register.filter
def human_bytes(value):
    """
    Convert a byte value into a human-readable format.
    """
    value = float(value)
    if value >= 1073741824:
        gigabytes = value / 1073741824
        size = '%.2f GB' % gigabytes
    elif value >= 1048576:
        megabytes = value / 1048576
        size = '%.2f MB' % megabytes
    elif value >= 1024:
        kilobytes = value / 1024
        size = '%.2f KB' % kilobytes
    else:
        size = '%.2f B' % value
    return size


@register.filter
def timestamp(value):
    """
    Timestamp to elapsed time format.
    """
    return timedelta(0, int(value))


@register.filter
def datetimestamp(value):
    """
    Timestamp to date/time format.
    """
    return datetime.fromtimestamp(int(value)).strftime('%x %X')


@register.filter
def yes_no(value):
    """
    Convert integer or boolean to words.
    """
    if not value:
        return ''
    if int(value):
        return _("Yes")
    else:
        return _("No")
