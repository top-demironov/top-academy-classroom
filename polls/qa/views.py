from django.http import HttpResponse, Http404
from django.shortcuts import render

from qa.models import Question, Choice


def index(request):
	questions = Question.objects.all()
	return HttpResponse('<script>alert("asdf")</script>')


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
		choices = Choice.objects.filter(question_id=question.id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'detail.html',
								{'question': question, 'choices': choices})


def results(request, question_id):
	response = f"You're looking at the results of question {question_id}."
	return HttpResponse(response)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)