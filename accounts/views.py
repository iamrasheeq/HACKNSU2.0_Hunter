from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'accounts/dashboard.html')
def clients(request):
    return render(request,'accounts/clients.html')
def vendors(request):
    return render(request,'accounts/vendors.html')
def products(request):
    return render(request,'accounts/products.html')


# Create your views here.
