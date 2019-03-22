from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'practice-test'),
	path('api', views.api, name = 'practice-post')
]