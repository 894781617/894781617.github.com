#coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from my_app.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                        url(r'^admin/', include(admin.site.urls)),
                       (r'^$', index),
                        url(r'^tags/$', tag, name='tags'),
                        url(r'^archive/$', archive, name='archive'),
                        # url(r'^tags/(?P<tag_name>\w+)$', detail, name='tag_name'),
                        url(r'^detial$', detail, name='tag_name'),
                       url(r'^article$', article, name='article'),
                        url(r'^comment/$',comment, name='comment'),
)
