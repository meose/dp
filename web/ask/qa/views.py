from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage

from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

# Create your views here.
# Login
def loginview(request):
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
		'form' : form,
		'user': request.user,
		'session': request.session})

# Signup
def signupView(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data["username"]
			password = form.raw_passeord
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()

	return render(request, 'signup.html', {
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
