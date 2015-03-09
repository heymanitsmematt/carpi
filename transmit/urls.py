from django.conf.urls import patterns
from transmit.views import TransmitView, Player

urlpatterns = patterns('transmit/',
    (r'^sing/', TransmitView.as_view()),
    (r'^player/(?P<action>.*)$', Player.as_view()),
)
