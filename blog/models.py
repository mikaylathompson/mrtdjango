from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	author = models.CharField(max_length=50)
	text = models.TextField()
	edit_date = models.DateTimeField('date last edited')

	def __unicode__(self):
		return self.title

	def next_id(self):
		return self.id + 1

	def prev_id(self):
		return self.id - 1

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def by_guest_author(self):
		my_names = ["Mikayla", "MRT", "Mikayla Thompson"]
		return self.author not in my_names

	class Meta:
		ordering = ('pub_date',)

			

class Comment(models.Model):
	post = models.ForeignKey(Post)
	commentor = models.CharField(max_length=50)
	com_text = models.TextField()
	com_date = models.DateTimeField('date commented')

	def __unicode__(self):
		return "by " + self.commentor + ': "' + self.com_text + '"'

	class Meta:
		ordering = ('com_date',)

class Tag(models.Model):
	posts = models.ManyToManyField(Post)
	label = models.CharField(max_length=50)

	def __unicode__(self):
		return self.label


