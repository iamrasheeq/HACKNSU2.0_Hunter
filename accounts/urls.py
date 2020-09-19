from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='dashboard'),
    path('clients/', views.clients,name='clients'),
    path('products/', views.products,name='products'),
    path('vendors/', views.vendors),
]
