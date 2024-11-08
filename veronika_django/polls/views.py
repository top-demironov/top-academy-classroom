from django.shortcuts import render

from polls.models import Question


def index(request):
	questions = Question.objects.all()
	return render(request, 'index.html',
								{'questions': questions})


def detail(request, question_id):
	question = Question.objects.get(pk=question_id)
	return render(request, 'detail.html',
								{'question': question})