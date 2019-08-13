# blog views.py
from django.shortcuts import render

# Create your views here.

def blogPage(request):

	context = {'nbar' : 'blog'}

	return render(request, 'Blog/blog.html', context)