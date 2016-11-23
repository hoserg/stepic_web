from django.conf.urls import patterns, include, url
from qa import views

#app_name = 'qa'
urlpatterns = [
    url(r'^$', 'views.proba'),
    url(r'^login/$', 'views.proba'),
    url(r'^signup/$', 'views.proba'),
    url(r'^question/(<qid>\d+)/$', 'views.question'),
    url(r'^ask/$', 'views.proba'),
    url(r'^popular/$', 'views.popular'),
    url(r'^new/$', 'views.proba'),       
]
