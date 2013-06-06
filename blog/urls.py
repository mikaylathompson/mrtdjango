from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
	# ex: /blog/
	url(r'^$', views.index, name='index'),
	# ex: /blog/3/
	url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
	# ex: /write/
	url(r'^write/$', views.write, name='write')
)