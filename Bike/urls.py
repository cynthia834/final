
from django.contrib import admin
from django.urls import path

from Bike import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('lists/', views.bicycle_list, name='bicycle_list'),
    path('upload/', views.upload_bicycle, name='upload_bicycle'),
    path('',views.register, name='register'),
    path('login/',  views.login, name='login'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
