from django.conf.urls import url
from music_store import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.DefaultUserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.DefaultUserDetail.as_view()),

    url(r'^listeners/$', views.ListenerUserList.as_view()),
    url(r'^listeners/(?P<pk>[0-9]+)/$', views.ListenerUserDetail.as_view()),

    url(r'^labelusers/$', views.LabelUserList.as_view()),
    url(r'^labelusers/(?P<pk>[0-9]+)/$', views.LabelUserDetail.as_view()),

    url(r'^track_labels/$', views.TrackLabelList.as_view()),
    url(r'^track_labels/(?P<pk>[0-9]+)/$', views.TrackLabelDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)