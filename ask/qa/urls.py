rom django.conf.urls import patterns, include, url
from qa import views

urlpatterns = patterns('',
    url(r'^/(\d+)/$', 'views.test'),
)
