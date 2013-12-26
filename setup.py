# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="django-memcache-admin",
    version='0.0.2',
    author="Ianaré Sévi",
    author_email="ianare@gmail.com",
    url="https://github.com/ianare/django-memcache-admin",
    license="LGPLv3+",
    keywords="memcached",
    description="Memcache admin for Django.",
    long_description=open("README.rst", "rt").read(),
    install_requires=[
        "Django>=1.6",
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
