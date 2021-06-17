from django.urls import path

from . import views

app_name = 'randomfortune'

urlpatterns = [
    path('', views.fortune, name='fortune'),
    path('home/', views.home, name='home'),

 ]
