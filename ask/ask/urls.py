from django.conf.urls import patterns, include, url
from ask import views

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'views.proba'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/(\d+)$', qa.views.test), #include(qa.urls)),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'views.proba'),
    url(r'^new/$', 'views.proba'),
]
