# -*- coding: utf-8 -*-

from twisted.application.service import Application
from app import twisted

application = Application('twisted-flask')
twisted.run(run_reactor=False)