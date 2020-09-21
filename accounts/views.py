from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    client_orders = Client_Order.objects.all()
    vendor_orders = Vendor_Order.objects.all()
    clients = Client.objects.all()
    vendors = Vendor.objects.all()

    total_clients = clients.count()

    total_orders = client_orders.count()
    complete = client_orders.filter(status="Complete").count()
    pending = client_orders.filter(status="Pending").count()

    context = {'client_orders':client_orders,'clients':clients,
    'vendor_orders':vendor_orders,'vendors':vendors,'total_orders':total_orders,
    'complete':complete,'pending':pending,'total_clients':total_clients}

    return render(request,'accounts/dashboard.html',context)

def clients(request):
    client_orders = Client_Order.objects.all()

    clients = Client.objects.all()
    context = {'client_orders':client_orders,'clients':clients}

    return render(request,'accounts/clients.html',context)

def vendors(request):
    vendor_orders = Vendor_Order.objects.all()
    vendors = Vendor.objects.all()
    context = {'vendors':vendors,'vendor_orders':vendor_orders}
    return render(request,'accounts/vendors.html',context)

def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def vprofile(request,pkey):
    vprofile = Vendor.objects.get(id=pkey)
    orders = vprofile.vendor_order_set.all()

    order_count = orders.count()

    context = {'vprofile':vprofile, 'orders':orders, 'order_count':order_count }
    return render(request,'accounts/vprofile.html',context)

def vorder(request):

    form = VendorOrderForm()
    if request.method == "POST":
        form = VendorOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request,'accounts/vorder.html',context)

def corder(request):

    form = ClientOrderForm()
    if request.method == "POST":
        form = ClientOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request,'accounts/corder.html',context)

def createVendor(request):

    form = VendorCreate()
    if request.method == "POST":
        form = VendorCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vendors/')


    context = {'form':form}
    return render(request,'accounts/vcreate.html',context)
def createClient(request):

    form = ClientCreate()
    if request.method == "POST":
        form = ClientCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients/')


    context = {'form':form}
    return render(request,'accounts/ccreate.html',context)

def vorderupdate(request,pkey):

    order = Vendor_Order.objects.get(id=pkey)
    form = VendorOrderForm(instance=order)

    if request.method == 'POST':
        form = VendorOrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
def corderupdate(request,pkey):

    order = Client_Order.objects.get(id=pkey)
    form = ClientOrderForm(instance=order)

    if request.method == 'POST':
        form = ClientOrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')



    context = {'form':form}
    return render(request,'accounts/corder.html',context)




def deleteOrder(request, pkey):
    order = Vendor_Order.objects.get(id=pkey)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request,'accounts/delete.html',context)

def deleteOrderC(request, pkey):
    order = Client_Order.objects.get(id=pkey)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request,'accounts/deleteC.html',context)
