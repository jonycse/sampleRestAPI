from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from piston.resource import Resource

admin.autodiscover()

#from api.bookapi.apiHandler import ApiHandler

urlpatterns = patterns('',

    #url(r'^bookapi/(?P<cat_id>\d+)/$', Resource(ApiHandler)),

    # Examples:
    # url(r'^$', 'sampleRestAPI.views.home', name='home'),
    # url(r'^sampleRestAPI/', include('sampleRestAPI.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #
    (r'^myapi/', include('api.apihandler.urls')),
)
