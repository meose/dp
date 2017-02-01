from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def quest(request, num):
	try:
		questioni = Question.objects.get(pk=num)
	except ObjectDoesNotExist:
		raise Http404()
	except ValueError:
		raise Http404()
	res = []

	for i in Answer.objects.all():
		if(i.question == questioni):
			res.append(i)	

	return render(request, 'question.html', 
    	{'title': questioni.title,
         'question': questioni,
         'answers' : res,
		})

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

	return render(request, 'main.html', 
    	{'title': 'Main Page',
         'paginator': paginator,
         'questions': page.object_list,
         'page': page, })

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

	return render(request, 'popular.html', 
    	{'title': 'Popular',
         'paginator': paginator,
         'questions': page.object_list,
         'page': page, })