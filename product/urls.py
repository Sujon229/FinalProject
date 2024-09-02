from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.show_product, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
