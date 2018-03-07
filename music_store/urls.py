from django.conf.urls import url
from music_store import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.DefaultUserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.DefaultUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)