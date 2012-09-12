from django.conf.urls import patterns, include, url

from piston.resource import Resource
from api.apihandler.bookapiHandler import BookApiHandler, BookApiCatHandler
urlpatterns = patterns('',
    url(r'^getbook/(?P<book_id>\d+)/$', Resource(BookApiHandler)),
    url(r'^getbook/(?P<book_id>\d+)/xml/$', Resource(BookApiHandler), { 'emitter_format': 'xml' }),


    url(r'^allbook/$', Resource(BookApiHandler)),
    url(r'^allbook/xml/$', Resource(BookApiHandler),{ 'emitter_format': 'xml' }),

    url(r'^category/(?P<cat_id>\d+)/$', Resource(BookApiCatHandler)),
    url(r'^category/(?P<cat_id>\d+)/xml/$', Resource(BookApiCatHandler), { 'emitter_format': 'xml' }),
)
