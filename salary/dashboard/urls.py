from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # ex: /dashboard/
    path('', views.index, name='index'),
    path('dom/', views.dom, name='dom'),
    path('home/', views.home, name='home'),
 ]
