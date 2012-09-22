'''
URL Mapping with handler
'''


from django.conf.urls import patterns, include, url

from piston.resource import Resource
from api.apihandler.bookapiHandler import BookApiHandler, BookApiCatHandler

from api.apihandler.bookapiExtendedHandler import BookApiExtendedHandler


urlpatterns = patterns('',
    url(r'^getbook/(?P<book_id>\d+)/$', Resource(BookApiHandler)),
    url(r'^getbook/(?P<book_id>\d+)/xml/$', Resource(BookApiHandler), { 'emitter_format': 'xml' }),


    url(r'^allbook/$', Resource(BookApiHandler)),
    url(r'^allbook/xml/$', Resource(BookApiHandler),{ 'emitter_format': 'xml' }),

    url(r'^category/(?P<cat_id>\d+)/$', Resource(BookApiCatHandler)),
    url(r'^category/(?P<cat_id>\d+)/xml/$', Resource(BookApiCatHandler), { 'emitter_format': 'xml' }),

    #bookapiExtended
    url(r'^extend/allbook/$', Resource(BookApiExtendedHandler)),
    url(r'^extend/allbook/xml/$', Resource(BookApiExtendedHandler), { 'emitter_format': 'xml' }),
)
