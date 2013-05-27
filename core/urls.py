from django.conf.urls import patterns, include, url
from core.views import HomeView
from core.views import AboutUsView

urlpatterns = patterns('',
  url(r'^$', HomeView.as_view()),
)