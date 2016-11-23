from django.conf.urls import patterns, include, url
from ask import views
from qa.views import *

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'newqa'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'popular'),
    url(r'^new/$', 'views.proba'),
]
