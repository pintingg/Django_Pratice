from django.urls import path
from . import views

urlpatterns = [
	path('', views.test, name = 'practice-test'),
	path('post', views.post, name = 'practice-post')
]