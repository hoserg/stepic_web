from django.conf.urls import patterns, include, url
#from qa import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'qa.views.newqa'),
    url(r'^login/$', 'qa.views.proba'),
    url(r'^signup/$', 'qa.views.proba'),
    url(r'^question/(?P<qid>\d+)/', 'qa.views.question'),
    url(r'^ask/$', 'qa.views.ask'),
    url(r'^popular/$', 'qa.views.popular'),
    url(r'^new/$', 'qa.views.proba'),       
]
