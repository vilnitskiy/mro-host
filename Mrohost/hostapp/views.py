from django.shortcuts import render
from models import Files

# Create your views here.
def home(request, link):
	file = Files.objects.filter(link = link)
	return file