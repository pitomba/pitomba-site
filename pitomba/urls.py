# coding: utf-8
from tornado.web import URLSpec

from pitomba.handlers.page import PageHandler

urls = (
    URLSpec(r'/(?P<page>index.html)?', PageHandler, name='home_index'),
    URLSpec(r'/(?P<context>.[\w-]+)/?', PageHandler, name='home'),
    URLSpec(r'/(?P<context>.[\w-]+)(?P<page>/index.html)?', PageHandler,
            name='context'),
)
