from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from music_store import views

urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^listeners/$', views.ListenerUserList.as_view(),
        name='listeners-list'),
    url(r'^listeners/(?P<pk>[0-9]+)/$', views.ListenerUserDetail.as_view(),
        name='listeners-detail'),

    url(r'^labelusers/$', views.LabelUserList.as_view(),
        name='labelusers-list'),
    url(r'^labelusers/(?P<pk>[0-9]+)/$', views.LabelUserDetail.as_view(),
        name='labelusers-detail'),

    url(r'^track_labels/$', views.TrackLabelList.as_view(),
        name='track_labels-list'),
    url(r'^track_labels/(?P<pk>[0-9]+)/$', views.TrackLabelDetail.as_view(),
        name='track_labels-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
