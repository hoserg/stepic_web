from django.conf.urls import patterns, include, url
from ask import views
#from django.ask import qa

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'views.newqa'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'views.popular'),
    url(r'^new/$', 'views.proba'),
]
