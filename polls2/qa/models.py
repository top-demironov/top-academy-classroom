from django.db import models


class Question(models.Model):
	text = models.CharField(max_length=200, verbose_name="text")
	pub_date = models.DateTimeField(verbose_name='Date published')

	def __str__(self):
		return self.text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.text