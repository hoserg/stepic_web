from django.conf.urls import patterns, include, url
from ask import views
#from django.ask import qa

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'views.proba'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/', 'views.proba'),
    url(r'^ask/$', 'qa.views.test'),
    url(r'^popular/$', 'views.proba'),
    url(r'^new/$', 'views.proba'),
]
