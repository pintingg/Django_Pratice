from django.contrib.staticfiles.templatetags import staticfiles
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def test(request):
	return render(request, 'practice/test.html')


def post(request):
	print(request.method)
	print(request.POST.get('a', 'Not get'))
	return JsonResponse({'data' : 'Succeed'})
