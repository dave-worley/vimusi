from django.conf.urls import patterns, include, url
urlpatterns = patterns('teachers.views',
    url(r'^$', 'list', name='teacher_list'),
    url(r'^signup/$', 'create_profile', name='teacher_profile'),
)
