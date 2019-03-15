from django.shortcuts import render

# Create your views here.

posts = [
	{
		'author'     : 'PT',
		'title'      : 'Blog post 1',
		'content'    : 'First post',
		'date_posted': 'Mar 14, 2019'
	},
	{
		'author'     : 'TP',
		'title'      : 'Blog post 2',
		'content'    : 'Second post',
		'date_posted': 'Mar 13, 2019'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
