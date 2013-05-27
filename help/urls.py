from django.conf.urls import patterns, include, url
from help.views import HelpView

urlpatterns = patterns('',
  url(r'^$', HelpView.as_view()),
)