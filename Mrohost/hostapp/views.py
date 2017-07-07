from django.shortcuts import render
from hostapp.forms import FileFieldForm
from hostapp.models import File
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from models import Files

# Create your views here.
"""
def home(request, link):
	file = Files.objects.filter(link = link)
	return file
"""
def home(request):
	if request.method == "POST":
		form = FileFieldForm(request.POST, request.FILES)
		files = request.FILES.getlist('file_field')
		if form.is_valid():
			for f in files:
				File.objects.create(url=f)
			return HttpResponseRedirect(reverse('main'))
	else:
		form = FileFieldForm()
		return render(request, 'base.html', {'form': form})