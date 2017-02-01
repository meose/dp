from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET

def response(request):
	return HttpResponse("200 OK")

def notResponse(request):
	raise Http404()