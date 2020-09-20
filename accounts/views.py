from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    client_orders = Client_Order.objects.all()
    vendor_orders = Vendor_Order.objects.all()
    clients = Client.objects.all()
    vendors = Vendor.objects.all()

    context = {'client_orders':client_orders,'clients':clients,
    'vendor_orders':vendor_orders,'vendors':vendors}

    return render(request,'accounts/dashboard.html',context)

def clients(request):
    return render(request,'accounts/clients.html')
def vendors(request):
    return render(request,'accounts/vendors.html')
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})


# Create your views here.
