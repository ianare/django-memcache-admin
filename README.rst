Django Memcache Admin
=====================

.. image:: https://pypip.in/v/django-memcache-admin/badge.png
        :target: https://crate.io/packages/django-memcache-admin
.. image:: https://pypip.in/d/django-memcache-admin/badge.png
        :target: https://crate.io/packages/django-memcache-admin

Memcache admin for Django.

* Show cluster information.
* Show a server's statistics.
* Show a server's slabs.
* Flush the cluster.

...more to come!


Install
-------

Install via pip::

    pip install django-memcache-admin

Add ``memcache_admin`` to ``INSTALLED_APPS`` in your setting.py file.

The application will be available in the admin panel.


Compatibility
-------------

* Django 1.6 and up.
* For best results, `python-memcached <https://pypi.python.org/pypi/python-memcached/>`_ should be used.
* `pylibmc <https://pypi.python.org/pypi/pylibmc/>`_ can be used, but not all information will be available.


Acknowledgements
----------------

Some ideas taken from the
`django-memcache-status <https://pypi.python.org/pypi/django-memcache-status/1.1/>`_
and `django-memcached2 <https://pypi.python.org/pypi/django-memcached2/>`_ projects


License
-------

GNU Lesser General Public License, version 3.
