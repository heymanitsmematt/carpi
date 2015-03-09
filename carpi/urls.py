from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import Home
import transmit
import driver

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^transmit/', include('transmit.urls')),
    url(r'^driver/', include('driver.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
