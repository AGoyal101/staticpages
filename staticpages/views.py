from django.shortcuts import render

# Create your views here.

# staticpages/views.py
from django.http import HttpResponse

def home_page_view(request):
	return HttpResponse("My staticpages homepage.")

def about_page_view(request):
	return HttpResponse("About page.")
