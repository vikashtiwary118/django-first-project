from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world_view(request):
	user=request.user
	print(user)
	return HttpResponse('<h1>Hello This is Response From Django Application</h1>')

