from django.conf.urls.defaults import *
from fifiant.search.models import Search
press_list_dict={
'queryset': Search.objects.all(),
'template_name': 'search/list.html',
'allow_empty': False,
'template_object_name': 'search',
}
urlpatterns = patterns('',
	(r'^(?P<pid>\d+)/$', 'fifiant.search.views.detail_search'),
	(r'^$', 'fifiant.search.views.searchs'),
	#(r'list/$','django.views.generic.list_detail.object_list',press_list_dict),
	#(r'$', 'django.views.generic.simple.redirect_to',{'url': '/press/list/'})
)

