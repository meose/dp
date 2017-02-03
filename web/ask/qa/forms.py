from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
	username = forms.CharField( max_length=100, required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=False)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError('No username')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password')
		if not password:
			raise forms.ValidationError('No password')
		return password

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError('Invalid password or username')
		if not user.check_password(password):
			raise forms.ValidationError('Invalid password or username')

class SignupForm(forms.Form):
	username = forms.CharField(max_length=100, required=False)
	email = forms.EmailField(required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=False)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError('Not username')
		try:
			User.objects.get(username=username)
			raise forms.ValidationError('This username is not availible')
		except User.DoesNotExist:
			pass
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError('Not email')
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		if not password:
			raise forms.ValidationError('Not password')
		self.raw_passeord = password
		return make_password(password)

	def save(self):
		user = User(**self.cleaned_data)
		user.save()
		return user

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		return self.cleaned_data

	def save(self):
		question = Question(**self.cleaned_data)
		question.author_id = self._user.id
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
		return self.cleaned_data

	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.author_id = self._user.id
		answer.save()
		return answer

