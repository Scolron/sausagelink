from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sharedUrl.views',
    url(r'^group/$', 'showGroup'),
    url(r'^$', 'showGroup'),
    url(r'^add/$', 'add'),
    url(r'^group/add$', 'add'),
)
