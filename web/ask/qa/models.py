from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-added_at")
	def popular(self):
		return self.order_by("-rating")

# Create your models here
class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(default="", max_length=1024)
	text = models.TextField(default="")
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, related_name="auth_q")
	likes = models.ManyToManyField(User, related_name="like_q")
	def __str__(self):
		return self.title
	def get_url(self):
		return "/question/{}/".format(self.id)
	def __unicode__(self):
		return self.title

class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True)
	author = models.ForeignKey(User, null=True)
	def __str__(self):
		return self.text