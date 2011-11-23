from django.conf.urls.defaults import *
from fifiant.topic.models import Topic
press_list_dict={
'queryset': Topic.objects.all(),
'template_name': 'search/list.html',
'allow_empty': False,
'template_object_name': 'search',
}
urlpatterns = patterns('',
	(r'^(?P<pid>\d+)/$', 'fifiant.topic.views.detail_topic'),
	(r'^$', 'fifiant.topic.views.topics'),
	#(r'list/$','django.views.generic.list_detail.object_list',press_list_dict),
	#(r'$', 'django.views.generic.simple.redirect_to',{'url': '/press/list/'})
)

