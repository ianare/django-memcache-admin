Django Memcache Admin
=====================

.. image:: https://pypip.in/v/django-memcache-admin/badge.png
        :target: https://crate.io/packages/django-memcache-admin
.. image:: https://pypip.in/d/django-memcache-admin/badge.png
        :target: https://crate.io/packages/django-memcache-admin

Memcache admin for Django.

* Show cluster information, optionally auto-updated.
* Show a server's statistics.
* Show a server's slabs.
* Flush the cluster.
* Compatible with default admin and Bootstrap.

...more to come!

This module is still in *beta status*: more testing is needed.


Install
-------
Install via pip::

    pip install django-memcache-admin

Add ``memcache_admin`` to ``INSTALLED_APPS`` in your ``settings.py`` file.

Update the database::

    python manage.py syncdb

The application will now be available in the admin panel.


Permissions
-----------
To use this module, a user must have access to the Django admin panel and have *change* permissions on the
``memcache_admin | Memcache Dashboard`` model.

Setting *add* or *delete* permissions has no effect, they are always false.


Settings
--------
In your ``settings.py`` file, you can add a dictionary called ``MEMCACHE_ADMIN``.

The following key/value settings are available:

REFRESH_RATE — integer
  Sets the auto-update refresh rate in milliseconds for the server information in the dashboard.
  Note that auto-updating must still be activated in the dashboard for this to take effect.
  If set to ``None``, refreshing will be disabled (unavailable in the dashboard interface).
  Default is 5000 milliseconds (5 seconds).

CACHE — string
  The cache definition to use. Default is "default".


Compatibility
-------------
* Django 1.6 and 1.7
* For best results, `python-memcached <https://pypi.python.org/pypi/python-memcached/>`_ should be used.
* `pylibmc <https://pypi.python.org/pypi/pylibmc/>`_ can be used, but not all information will be available.

This library is compatible with python 2 and 3, however the memcache packages above are only python2 compatible.


Acknowledgements
----------------
Some ideas taken from the
`django-memcache-status <https://pypi.python.org/pypi/django-memcache-status/1.1/>`_
and `django-memcached2 <https://pypi.python.org/pypi/django-memcached2/>`_ projects


License
-------
GNU Lesser General Public License, version 3.
