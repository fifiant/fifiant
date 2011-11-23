# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from fifiant.search.models import Search
from django.template import loader, Context
from django.shortcuts import get_object_or_404, get_list_or_404

def detail_search(request, pid):
	try:
	    p = get_object_or_404(Search, id=pid)
            t = loader.get_template('search/body.html')
            c = Context({'search': p})
            rendered_template = t.render(c)
            return HttpResponse(rendered_template)
	except Search.DoesNotExist:
            return HttpResponseNotFound('Press Release NOt Found')

def searchs(request):
	pl = get_list_or_404(Search)
	t = loader.get_template('search/search.html')
	c = Context({'searchs': pl})
	return HttpResponse(t.render(c))
