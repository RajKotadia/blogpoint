from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title