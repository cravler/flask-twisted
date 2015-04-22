# -*- coding: utf-8 -*-

from twisted.web.resource import Resource

class WSGIRootResource(Resource):
    def __init__(self, wsgiResource, children):
        """
        Creates a Twisted Web root resource.
        """
        Resource.__init__(self)
        self._wsgiResource = wsgiResource
        self.children = children

    def getChild(self, path, request):
        request.prepath.pop()
        request.postpath.insert(0, path)
        return self._wsgiResource
