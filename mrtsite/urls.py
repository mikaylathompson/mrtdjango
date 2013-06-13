from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^registration/register/$', views.register),
)
