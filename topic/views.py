# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from fifiant.topic.models import Topic
from django.template import loader, Context
from django.shortcuts import get_object_or_404, get_list_or_404

def detail_topic(request, pid):
	try:
	    p = get_object_or_404(Topic, id=pid)
            t = loader.get_template('topic/body.html')
            c = Context({'topic': p})
            rendered_template = t.render(c)
            return HttpResponse(rendered_template)
	except Topic.DoesNotExist:
            return HttpResponseNotFound('Press Release NOt Found')

def topics(request):
	pl = get_list_or_404(Topic)
	t = loader.get_template('topic/topic.html')
	c = Context({'topics': pl})
	return HttpResponse(t.render(c))
