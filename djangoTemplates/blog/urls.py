from django.urls import path

from blog import views

urlpatterns = [
	path('', views.home, name='home'),
	path('post/<int:id>', views.detail, name='detail'),
]