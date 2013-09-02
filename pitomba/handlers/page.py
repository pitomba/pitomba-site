# coding: utf-8
from pitomba import settings
from tornado.web import RequestHandler


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        if kwargs.get('context'):
            self.render("%s.html" % kwargs['context'],
                        SERVER_NAME=settings.SERVER_NAME)
        else:
            self.render("index.html", SERVER_NAME=settings.SERVER_NAME)
