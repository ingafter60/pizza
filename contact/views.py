# contact views.py
from django.shortcuts import render

# Create your views here.

def contactPage(request):

	context = {'nbar' : 'contact'}

	return render(request, 'Contact/contact.html', context)