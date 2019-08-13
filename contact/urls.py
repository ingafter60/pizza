# contact urls.py
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
	path('', views.contactPage, name='contactPage')
]