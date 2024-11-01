from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	a = 3
	b = 4
	return HttpResponse(f'{a} + {b} = {a + b}')
