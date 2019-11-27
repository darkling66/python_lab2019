from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Temperatue Sensor Works')

# Create your views here.
