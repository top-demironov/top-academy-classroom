from django.urls import path

from homework1 import views


urlpatterns = [
    path('', views.index, name='index'),
]
