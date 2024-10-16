from django.db import models


class Task(models.Model):
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=256)
	completed = models.BooleanField()
