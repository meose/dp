from django.http import HttpResponse, Http404

def response(request):
	return HttpResponse("200 OK")

def notResponse(request):
	raise Http404()