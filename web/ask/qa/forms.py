from django import forms
from .models import Question, Answer
from django.forms import ModelForm

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def clean_question(self):
		question_id = self.cleaned_data['question']
		try:
			question = Question.objects.get(pk=question_id)
		except Question.DoesNotExist:
			question = None
		return question

	def clean(self):
		pass

	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.author_id = 1
		answer.save()
		return answer