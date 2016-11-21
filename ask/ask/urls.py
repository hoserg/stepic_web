from django.conf.urls import patterns, include, url
from ask import views

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'views.empty'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/(\d+)$', 'views.proba'),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'views.proba'),
    url(r'^new/$', 'views.proba'),
]
