from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from inventory.models import *
from inventory.forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def client(request):
    if request.method == "POST":  
        form = ClientsForm(request.POST)  
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clients')
    else:  
        form = ClientsForm()
        
    clients_list = clients.objects.order_by('id')
    clients_list_pass = {'clients_list':clients_list, 'form':form}
    return render(request, 'client.html', context=clients_list_pass)

def supplier(request):
    if request.method == "POST":  
        form = SuppliersForm(request.POST)  
        if form.is_valid():
            form.save()
            form = SuppliersForm()
            return HttpResponseRedirect('/suppliers')
    else:  
        form = SuppliersForm()
        
    suppliers_list = suppliers.objects.order_by('id')
    suppliers_list_pass = {'suppliers_list':suppliers_list, 'form':form}
    return render(request, 'supplier.html', context=suppliers_list_pass)