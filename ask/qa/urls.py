from django.conf.urls import patterns, include, url
from . import views

app_name = 'qa'
urlpatterns = [
    url(r'^(\d+)/$', 'views.question'),
]
