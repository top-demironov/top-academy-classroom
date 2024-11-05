from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
	return HttpResponse(f'sdf')


def news(request):
	return HttpResponse(f'НОВОСТИ УРААААА ')