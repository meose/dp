from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login
# Create your views here.
# Logout
def logout(request):
	sessid = request.COOKIES.get('sessiond')
	if sessid is not None:
		Session.objects.delete(key=sessid)
	url = request.GET.get('continue', '/')
	response = HttpResponseRedirect(url)
	response.delete_cookie('sessionid')
	return response

# Login
def loginview(request):
	error = ""
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
 			user = authenticate(username=username, password=password)
 			if user is not None:
 				if user.is_active:
 					login(request, user)
 			return HttpResponseRedirect('/')
	else:
		form = LoginForm()
		error = "Bad login or password"

	return render(request, 'login.html', {
		'error': error, 
		'form' : form,
		'user': request.user,
		'session': request.session})

# Signup
def signup(request):
	error = ''
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = request.POST.get('username')
			email = request.POST.get('email')
			password = request.POST.get('password')
			if user is not None:
				if user.is_active:
					login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
		error = "Bad login or password"

	return render(request, 'signup.html', {
		'error': error, 
		'form' : form, 
		'user' : request.user, 
		'session': request.session,
		})

# Question 
def quest(request, num):
	try:
		q = Question.objects.get(pk=num)
	except Question.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = request.user
			r = form.save()
			url = q.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm(initial={'question': q.id})
	
	return render(request, 'question.html', {
		'question': q,
		'form': form, 
		'user': request.user,
		'session': request.session
		})

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

	return render(request, 'source.html', {
		'title': 'Last Questions', 
		'paginator': paginator, 
		'question': page.object_list, 
		'page': page, 
		'user': request.user,
		'session': request.session
		})

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

	return render(request, 'source.html', {
		'title': 'Popular', 
		'paginator': paginator, 
		'question': page.object_list, 
		'page': page, 
		'user': request.user,
		'session': request.session
		})

# ASK Page
def askFormAction(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = request.user
			post = form.save()
			url = post.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()

	return render(request, 'ask.html', {
		'form': form, 
		'user': request.user,
		'session': request.session
		})
