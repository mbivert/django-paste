from django.urls import path

from . import views

app_name = 'paste'

urlpatterns = [
	path('',            views.index,   name='index'),
	path('new/',        views.new,     name='new'),
	path('p/<str:id>/', views.paste,   name='paste'),
]
