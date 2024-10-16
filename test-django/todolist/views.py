from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from todolist.models import Task


@login_required
def index(request):
	tasks = Task.objects.all()
	return render(request, 'index.html',
								context={'tasks': tasks})


def add(request):
	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		task = Task(name=name, description=description, completed=False)
		task.save()
		return render(request, 'add_task.html')

	return render(request, 'add_task.html')
