# services views.py
from django.shortcuts import render

# Create your views here.

def servicesPage(request):

	context = { 'nbar' : 'services'}

	return render(request, 'Services/services.html', context)