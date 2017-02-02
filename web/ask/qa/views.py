from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from qa.forms import AskForm, AnswerForm
import logging
# Create your views here.

# Question 
def quest(request, num):
	try:
		q = Question.objects.get(pk=num)
	except Question.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = 1
			form.save()
			url = q.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm(initial={'question': q.id})

	return render(request, 'question.html', {'question': q,'form': form, })

# Main page - list of questions
def main(request, *args, **kwargs):
	try:
		page = int(request.GET.get('page', 1))
	except TypeError:
		page = 1
	except ValueError:
		page = 1
	paginator = Paginator(Question.objects.new(), 10)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, 'source.html', {'title': 'Main Page', 'paginator': paginator, 'question': page.object_list, 'page': page, })

# Main page - list of popular questions
def popularQuestions(request, *args, **kwargs):
	try:
		page = int(request.GET.get('page', 1))
	except TypeError:
		page = 1
	except ValueError:
		page = 1
	paginator = Paginator(Question.objects.popular(), 10)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, 'source.html', {'title': 'Popular', 'paginator': paginator, 'question': page.object_list, 'page': page,})

# ASK Page
def askFormAction(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = 1
			post = form.save()
			url = post.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask.html', {'form': form, })
