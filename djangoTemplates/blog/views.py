from django.shortcuts import render

from blog.models import Post


def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html', context={'posts': posts})


def detail(request, id):
	post = Post.objects.get(pk=id)
	return render(request, 'blog/detail.html', context={'post': post})