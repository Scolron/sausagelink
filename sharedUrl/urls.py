from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sharedUrl.views',
    url(r'^$', 'home'),
    url(r'^home/$', 'home'),
    url(r'^add/$', 'confirm'),
    url(r'^confirm/', 'confirm'),
    url(r'^user/(?P<user>.*)/$', 'user'),
)
