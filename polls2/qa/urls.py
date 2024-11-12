from django.urls import path, re_path

from qa import views


urlpatterns = [
    path('', views.index, name='index'),
    path('qa/<int:question_id>', views.detail, name='detail'),
    path('qa/', views.qa, name='qa'),
    # re_path(r'^qa/.*?$', views.redirect_qa, name='detail'),
]

