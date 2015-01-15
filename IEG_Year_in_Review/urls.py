from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('end_of_year_information.urls')),
    url(r'^admin/', include(admin.site.urls)),
)