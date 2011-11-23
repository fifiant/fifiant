from django.conf.urls.defaults import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
site_media = os.path.join(os.path.dirname(__file__), 'site_media')
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fifiant.views.home', name='home'),
    # url(r'^fifiant/', include('fifiant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),

    # Search management
    (r'^search/', include('fifiant.search.urls')),
    # Topic management
    (r'^topic/', include('fifiant.topic.urls')),
    # work management
    (r'^work/', include('fifiant.work.urls')),
    # main management
    url(r'^$', include('fifiant.main.urls')),
)
