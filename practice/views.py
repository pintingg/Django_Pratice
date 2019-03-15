from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
	return render(request, 'practice/test.html')

def post(request):

	return HttpResponse('<h1>received</h1>')