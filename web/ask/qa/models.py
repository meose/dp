from __future__ import unicode_literals
from django.db import models, connection
from django.contrib.auth.models import User

# Create managers of your models here
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-added_at")
	def popular(self):
		return self.order_by("-rating")

# Create your models here
class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=200)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="q_author")
	likes = models.ManyToManyField(User, related_name="q_likes")
	def get_url(self):
		return '/question/%d/' % self.pk
	def __unicode__(self):
		return self.title
			
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	question = models.ForeignKey(Question, related_name="ansToQ")
	author = models.ForeignKey(User, related_name="a_author")
	def __unicode__(self):
		return self.text