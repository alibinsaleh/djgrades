from django.urls import path
from grades import views

urlpatterns = [
	path('home/', views.home),
]