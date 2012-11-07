'''
URL Mapping with handler
'''


from django.conf.urls import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.apihandler.bookapiHandler import BookApiHandler, BookApiCatHandler

from api.apihandler.bookapiExtendedHandler import BookApiExtendedHandler
from django.views.decorators.cache import cache_page

auth = HttpBasicAuthentication()
ad = {'authentication': auth}

#TODO: add this api definition to readme
add_book_handler = Resource(handler=BookApiExtendedHandler, **ad)

#TODO: add category from API
#add_category_handler = Resource(handler=BookApiExtendedHandler, **ad)

urlpatterns = patterns('',
    url(r'^getbook/(?P<book_id>\d+)/$', Resource(BookApiHandler)),
    url(r'^getbook/(?P<book_id>\d+)/xml/$', Resource(BookApiHandler), { 'emitter_format': 'xml' }),


    url(r'^allbook/$', Resource(BookApiHandler)),
    url(r'^allbook/xml/$', Resource(BookApiHandler),{ 'emitter_format': 'xml' }),

    url(r'^category/(?P<cat_id>\d+)/$', Resource(BookApiCatHandler)),
    url(r'^category/(?P<cat_id>\d+)/xml/$', Resource(BookApiCatHandler), { 'emitter_format': 'xml' }),

    #bookapiExtended
    url(r'^extend/allbook/$', Resource(BookApiExtendedHandler)),
    #url(r'^extend/allbook/xml/$', Resource(BookApiExtendedHandler), { 'emitter_format': 'xml' }),

    url(r'^extend/allbook/xml/$', cache_page(60*1)(Resource(BookApiExtendedHandler)), { 'emitter_format': 'xml' }),

    url(r'^extend/category/(?P<cat_id>\d+)/$', Resource(BookApiExtendedHandler)),
    url(r'^extend/category_name/(?P<cat_name>\w+)/$', Resource(BookApiExtendedHandler)),

    # POST API
    url(r'^extend/add_book/$', add_book_handler),
   # url(r'^extend/add_category/$', Resource(add_category_handler)),
)
