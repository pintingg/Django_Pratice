from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

# Create your views here.

def home(request):
	return render(request, 'practice/test.html')

@csrf_exempt
def api(request):
	if request.method != 'POST': return HttpResponseBadRequest('unsupported type of request')
	content_type = request.META.get('CONTENT_TYPE', 'json')
	if content_type == 'application/x-www-form-urlencoded':
		data = request.POST
		print(request.POST)
	elif content_type == 'application/json':
		data = json.loads(request.body)
		print(request.body)
	else:
		return HttpResponseBadRequest('nunsupported type of content')
	if data:
		print('{} is {}.'.format(data['text'], data['type']))
		return JsonResponse({'data' : 'Hello World.'})
	else:
		return HttpResponseBadRequest('No data is received')
