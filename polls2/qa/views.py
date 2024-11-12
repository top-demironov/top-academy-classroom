from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from qa.models import Question, Choice


def index(request):
	questions = Question.objects.all()
	return render(request, 'index.html',
								{'questions': questions})


def detail(request, question_id):
	question = Question.objects.get(pk=question_id)
	choices = Choice.objects.filter(question_id=question.id)
	return render(request, 'detail.html',
								{'question': question,
								 				'choices': choices})

def qa(request):
	return HttpResponse('QA page')


def redirect_qa(request):
	return redirect(reverse('qa'))


def error(request, exception):
	print(request)
	return redirect(reverse('index'))