from django.conf.urls import patterns, include, url
#from ask import views
#from ask.qa.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('qa.urls')),
]
