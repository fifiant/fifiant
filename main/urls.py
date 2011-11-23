from django.conf.urls.defaults import *
from fifiant.main.models import Paper

urlpatterns = patterns('',
	#(r'^(?P<pid>\d+)/$', 'fifiant.main.views.index'),
	(r'^$', 'fifiant.main.views.index'),
	#(r'list/$','django.views.generic.list_detail.object_list',press_list_dict),
	#(r'$', 'django.views.generic.simple.redirect_to',{'url': '/press/list/'})
)

