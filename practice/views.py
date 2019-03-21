from django.contrib.staticfiles.templatetags import staticfiles
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

def test(request):
	return render(request, 'practice/test.html')

@csrf_exempt
def post(request):
	data = request.POST
	if data:
		print('{} is {}.'.format(data['a'], data['b']))
		return JsonResponse({'data' : 'Succeed'})
	else:
		return HttpResponseNotFound()
