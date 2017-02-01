from django.db import models
from django.contrib.auth.models import User

# Create managers of your models here
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-added_at")
	def popular(self):
		return self.order_by("-rating")

# Create your models here
class Question(models.Model):
	cobjects = QuestionManager()
	title = models.CharField(default="", max_length=1024)
	text = models.TextField(default="")
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="q_author")
	likes = models.ManyToManyField(User, related_name="q_likes")
	def __str__(self):
		return self.title
	def get_url(self):
		return "/question/{}/".format(self.id)
			
class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	question = models.ForeignKey(Question, related_name="ansToQ")
	author = models.ForeignKey(User, related_name="a_author")
	def __str__(self):
		return self.text