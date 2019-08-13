# home views.py
from django.shortcuts import render

# Create your views here.

def homePage(request):

	context = {
		'nbar': 'home'
	}

	return render(request, 'Home/index.html', context)