rom django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^/(\d+)/$', 'views.test'),
)
