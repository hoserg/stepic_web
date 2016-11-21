rom django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/(\d+)/$', views.test),
)
