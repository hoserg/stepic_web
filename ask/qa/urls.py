rom django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^(\d+)/$', 'views.test'),
]
