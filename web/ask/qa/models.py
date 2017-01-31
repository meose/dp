from __future__ import unicode_literals
from django.db import models, connection
from django.contrib.auth.models import User

# Create managers of your models here
class QuestionManager(models.Manager):
	def new(self):
		cursor = connection.cursor()
		cursor.execute('''
			SELECT * FROM base.qa_question order by added_at DESC;
			''')
		result = []
		for row in cursor.fetchall():
			p = self.model(id=row[0], title=row[1], text=row[2], added_at=row[3], rating = row[4], author_id = row[5])
			result.append(p)
		return result
	def popular(self):
		cursor = connection.cursor()
		cursor.execute('''
			SELECT * FROM base.qa_question order by rating DESC;
			''')
		result = []
		for row in cursor.fetchall():
			p = self.model(id=row[0], title=row[1], text=row[2], added_at=row[3], rating = row[4], author_id = row[5])
			result.append(p)
		return result

# Create your models here
class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=200)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="q_author")
	likes = models.ManyToManyField(User, related_name="q_likes")
			
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	question = models.ForeignKey(Question, related_name="ansToQ")
	author = models.ForeignKey(User, related_name="a_author")
