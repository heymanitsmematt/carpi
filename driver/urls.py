from django.conf.urls import patterns, include, url
from driver.views import Drive

urlpatterns = patterns('driver/',
    url(r'^drive/$', Drive.as_view()),
)
