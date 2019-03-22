from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

def home(request):
	return render(request, 'practice/test.html')

@csrf_exempt
def api(request):
	data = request.POST
	if data:
		print('{} is {}.'.format(data['a'], data['b']))
		return JsonResponse({'data' : 'Hi, Ming.'})
	else:
		return render(request, 'practice/errorpage.html')
