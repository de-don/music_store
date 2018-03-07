from django.conf.urls import url
from music_store import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^listeners/$', views.ListenerList.as_view()),
    url(r'^listeners/(?P<pk>[0-9]+)/$', views.ListenerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)