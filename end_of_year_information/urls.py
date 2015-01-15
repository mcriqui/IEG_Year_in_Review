from django.conf.urls import patterns, include, url
from django.contrib import admin
from end_of_year_information import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(admin.site.urls)),
    url(r'^$', views.get_template, name="get_template"),
    url(r'^highlights/$', views.return_highlights, name="return_highlights"),
    url(r'^new/$', views.return_new, name="return_new"),
    url(r'^who/$', views.return_who_here, name="return_who_here"),
    url(r'^types/$', views.return_types_of_events, name="return_types_of_events"),
    url(r'^about/$', views.return_about_the_center, name="return_about_the_center"),
    url(r'^facility/$', views.return_facility, name="return_facility"),
    url(r'^team/$', views.return_team, name="return_team")
)
