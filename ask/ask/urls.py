from django.conf.urls import patterns, include, url
from ask import views, qa
#from ask import qa

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^$', 'qa.views.newqa'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'qa.views.popular'),
    url(r'^new/$', 'views.proba'),
]
