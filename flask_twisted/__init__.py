# -*- coding: utf-8 -*-

import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from .decorators import defer_to_thread
from .resource import WSGIRootResource
from observable import Observable

class Twisted(Observable):

    def __init__(self, app=None):
        self.app = None
        self.resources = {}

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.run = self.run

    def add_resource(self, name, resource):
        self.resources[name] = resource

    def create_site(self, resource, **options):
        return Site(resource)

    def run_simple(self, app, host, port, **options):
        self.trigger('run', app)

        if app.debug:
            log.startLogging(sys.stdout)

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = self.create_site(WSGIRootResource(resource, self.resources), **options)

        reactor.listenTCP(int(port), site, interface=host)

        if 'run_reactor' in options and options['run_reactor'] is False:
            pass
        else:
            reactor.run()

    def run(self, host=None, port=None, debug=None, **options):
        app = self.app
        if app is None and 'app' in options:
            app = options['app']
        if app is None:
            raise Exception('"app" not defined')

        if host is None:
            host = '127.0.0.1'

        if port is None:
            server_name = app.config['SERVER_NAME']
            if server_name and ':' in server_name:
                port = int(server_name.rsplit(':', 1)[1])
            else:
                port = 5000

        if debug is not None:
            app.debug = bool(debug)

        self.run_simple(app, host, port, **options)
