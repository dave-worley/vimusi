from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import AboutUsView
from core.views import HomeView
from core.views import TermsView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^teachers/', include('teachers.urls')),
    url(r'^classes/', include('class_sessions.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^about/$', AboutUsView.as_view(), name='about_us'),
    url(r'^terms/$', TermsView.as_view(), name='policy_terms'),
    url(r'^help/', include('help.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
)