Django Memcache Admin
=====================

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
* For best results, `python-memcached` should be used.
* `pylibmc` can be used, but not all information will be available.


Acknowledgements
----------------

Some ideas taken from the `django-memcache-status` and `django-memcached2` projects.


License
-------

GNU Lesser General Public License, version 3.