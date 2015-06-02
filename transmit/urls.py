from django.conf.urls import patterns
from transmit.views import TransmitView, Player, RefreshMedia

urlpatterns = patterns('transmit/',
    (r'^sing/', TransmitView.as_view()),
    (r'^play/(?P<id>[0-9]+)/$', Player.as_view()),
    (r'^RefreshMedia/', RefreshMedia.as_view()),
)
