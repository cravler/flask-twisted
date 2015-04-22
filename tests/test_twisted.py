# -*- coding: utf-8 -*-

import unittest

from flask import Flask
from flask.ext.twisted import Twisted

class TestTwisted(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_run(self):
        app = Flask(__name__)
        twisted = Twisted()
        self.assertNotEqual(twisted.run, app.run)
        twisted.init_app(app)
        self.assertEqual(twisted.run, app.run)

        app = Flask(__name__)
        twisted = Twisted(app)
        self.assertEqual(twisted.run, app.run)

    def test_run_trigger(self):
        app = Flask(__name__)
        twisted = Twisted(app)

        @twisted.on('run')
        def on_run(_app):
            self.assertEqual(app, _app)

        self.assertTrue('run' in twisted.events and twisted.events['run'])

        app.run(host='127.0.0.1', port=5000, run_reactor=False)
        twisted.run(host='127.0.0.1', port=5001, run_reactor=False)
        twisted.run_simple(app=app, host='127.0.0.1', port=5002, run_reactor=False)

if __name__ == '__main__':
    unittest.main()
