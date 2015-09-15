# -*- coding: utf-8 -*-
"""
Flask-Twisted
-------------

Simple integration of Flask and Twisted
"""
from setuptools import setup

setup(
    name='Flask-Twisted',
    version='0.1.1',
    url='http://github.com/cravler/flask-twisted/',
    license='MIT',
    author='Sergei Vizel',
    author_email='sergei.vizel@gmail.com',
    description='Simple integration of Flask and Twisted',
    long_description=__doc__,
    py_modules=['flask_twisted'],
    packages=['flask_twisted'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'Twisted', 'observable'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)