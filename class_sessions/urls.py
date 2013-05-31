from django.conf.urls import patterns, include, url
from class_sessions.views import ClassProfileView
from class_sessions.views import ClassListView
from class_sessions.views import ClassRequestView
urlpatterns = patterns('',
    url(r'^$', ClassListView.as_view(), name='class_list'),
    url(r'^(?P<class_profile>\w+)/$', ClassProfileView.as_view(), name='class_profile'),
    url(r'^request/(?P<class_id>\w+)/$', ClassRequestView.as_view(), name='class_request'),
)
