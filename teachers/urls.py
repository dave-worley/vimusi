from django.conf.urls import patterns, include, url
from teachers.views import ProfileView
from teachers.views import TeacherListView
from teachers.views import DashboardView
urlpatterns = patterns('teachers.views',
    url(r'^$', TeacherListView.as_view(), name='teacher_list'),
    url(r'^dashboard/$', DashboardView.as_view(), name='teacher_dashboard'),
    url(r'^(?P<username>\w+)/$', ProfileView.as_view(), name='teacher_profile'),
)
