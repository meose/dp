from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')
