from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sharedUrl.views',
    url(r'^$', 'showGroupHarvard'),
    url(r'^add/$', 'add'),
    url(r'^confirm/$', 'confirm'),
    url(r'^theme/[hH]arvard', 'showGroupHarvard'),
    url(r'^theme/[Cc]orkboard', 'showGroupCorkboard'),
)
