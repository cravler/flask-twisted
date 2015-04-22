# -*- coding: utf-8 -*-

import functools
from twisted.internet import threads

def defer_to_thread(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        return threads.deferToThread(f, *args, **kwargs)
    return wrapped
