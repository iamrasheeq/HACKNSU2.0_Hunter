from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='dashboard'),
    path('clients/', views.clients,name='clients'),
    path('products/', views.products,name='products'),
    path('vendors/', views.vendors,name='vendors'),
    path('vprofile/<str:pkey>/', views.vprofile,name='vprofile'),
    path('vorder/', views.vorder,name='vorder'),
    path('corder/', views.corder,name='corder'),
    path('vorderupdate/<str:pkey>/', views.vorderupdate,name='vorderupdate'),
    path('corderupdate/<str:pkey>/', views.corderupdate,name='corderupdate'),
    path('deleteOrder/<str:pkey>/', views.deleteOrder,name='deleteOrder'),
    path('deleteOrderC/<str:pkey>/', views.deleteOrderC,name='deleteOrderC'),
    path('createVendor/', views.createVendor,name='createVendor'),
    path('createClient/', views.createClient,name='createClient'),
    path('addProduct/', views.addProduct,name='addProduct'),
    path('addTag/', views.addTag,name='addTag'),
]
