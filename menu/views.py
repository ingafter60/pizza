# menu views.py
from django.shortcuts import render

# Create your views here.

def menuPage(request):

	context = {
		'nbar': 'menu'
	}

	return render(request, 'Menu/menu.html', context)