# blog urls.py
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
	path('', views.blogPage, name='blogPage')
]