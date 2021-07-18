from django.urls import path
from grades import views

urlpatterns = [
	path('', views.home, name='home'),
	path('<int:year>/<str:month>/', views.home, name='home'),
]