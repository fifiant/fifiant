# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from fifiant.main.models import Paper
from django.template import loader, Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.mail import send_mail, BadHeaderError

def send_email(request):
    subject = request.POST.get('subject', 'Test')
    message = request.POST.get('message', 'Test')
    from_email = request.POST.get('from_email', 'admin@fifiant.com')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['fifiant@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/search/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def index(request):
	pl = get_list_or_404(Paper)
	t = loader.get_template('main/index.html')
	c = Context({'papers': pl})
	return HttpResponse(t.render(c))
	#return render_to_response('main/index.html', context_instance=RequestContext(request))
def topics(request):
	pl = get_list_or_404(Topic)
	t = loader.get_template('topic/topic.html')
	c = Context({'topics': pl})
	return HttpResponse(t.render(c))# Create your views here.
