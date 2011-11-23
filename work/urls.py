from django.conf.urls.defaults import *
from fifiant.work.models import Work
press_list_dict={
'queryset': Work.objects.all(),
'template_name': 'search/list.html',
'allow_empty': False,
'template_object_name': 'search',
}
urlpatterns = patterns('',
	(r'^work/(?P<pid>\d+)/$', 'fifiant.work.views.detail_work'),
	(r'work/$', 'fifiant.work.views.works'),
	#(r'list/$','django.views.generic.list_detail.object_list',press_list_dict),
	#(r'$', 'django.views.generic.simple.redirect_to',{'url': '/press/list/'})
)

