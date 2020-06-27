from django.shortcuts import render
from .models import Post, Tag


def home(request):

	posts = Post.objects.all().order_by('-date_published')
	tags = Tag.objects.all()

	context = {
		'posts': posts,
		'tags': tags,
	}
	return render(request, 'blog/index.html', context)


def about(request):
	return render(request, 'blog/about.html')