from django.contrib.auth.models import AbstractUser
from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class User(AbstractUser):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.username


class StatusTask(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	status = models.ForeignKey(StatusTask, on_delete=models.DO_NOTHING, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	due_date = models.DateField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	performers = models.ManyToManyField(User)


	def __str__(self):
		return self.title
