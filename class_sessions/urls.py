from django.conf.urls import patterns, include, url
from class_sessions.views import ClassProfileView
from class_sessions.views import ClassListView
urlpatterns = patterns('',
    url(r'^$', ClassListView.as_view(), name='class_profile_main'),
    url(r'^(?P<class_profile>\w+)/$', ClassProfileView.as_view(), name='class_profile'),
)
