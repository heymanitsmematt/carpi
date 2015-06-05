from django.conf.urls import patterns
from transmit.views import TransmitView, Player, RefreshMedia, YoutubeDownloader

urlpatterns = patterns('transmit/',
    (r'^sing/', TransmitView.as_view()),
    (r'^play/(?P<id>[0-9]+)/$', Player.as_view()),
    (r'^youtubesearch/(?P<URI>\w+)/(?P<query>\w+)/$', YoutubeDownloader.as_view()),
    (r'^youtubesearch/(?P<query>\w+)/$', YoutubeDownloader.as_view()),
    (r'^RefreshMedia/', RefreshMedia.as_view()),
)
