from django.conf.urls import patterns, include, url
from teachers.views import ProfileView
urlpatterns = patterns('teachers.views',
    url(r'^$', ProfileView.as_view(), name='teacher_mains'),
    url(r'^(?P<username>\w+)/$', ProfileView.as_view(), name='teacher_profile'),
)
