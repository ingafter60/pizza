# about views.py
from django.shortcuts import render

# Create your views here.

def aboutPage(request):

	context = {'nbar' : 'about'}

	return render(request, 'About/about.html', context)