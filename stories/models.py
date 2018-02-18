from django.db import models
from django.conf import settings


class Story(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	abstract = models.TextField()
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='stories'
	)
	slug = models.SlugField()

	def __str__(self):
		return self.title

class Chapter(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=255)
	number = models.IntegerField()
	content = models.TextField()
	story = models.ForeignKey(
		'stories.Story',
		on_delete=models.CASCADE,
		related_name='chapters'
	)
	slug = models.SlugField()

	def __str__(self):
		return self.title

class Place(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	story = models.ForeignKey(
		'stories.Story',
		on_delete=models.CASCADE,
		related_name='places'
	)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	story = models.ForeignKey(
		'stories.Story',
		on_delete=models.CASCADE,
		related_name='skills'
	)
	slug = models.SlugField()

	def __str__(self):
		return self.name

class Character(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	place = models.OneToOneField(
		'stories.Place',
		on_delete=models.CASCADE,
		related_name='place',
		null=True,
		blank=True
	)
	skill = models.ManyToManyField('stories.Skill')
	slug = models.SlugField()

	def __str__(self):
		return self.name