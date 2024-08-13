from django.urls import path

from . import views

app_name = 'paste'

urlpatterns = [
	path('p/<str:id>/', views.paste, name='paste'),
]
