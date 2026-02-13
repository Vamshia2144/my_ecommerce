from django.shortcuts import render, redirect
from merchant.models import MerchantDatabase
from django.contrib import messages

# Create your views here.
def merchant(request):
    return render(request, 'merchant.html')

def insert_merchant_data(request):
    if request.method == 'POST':
        mname = request.POST.get('mname')
        mnumber = request.POST.get('mnumber')
        memail = request.POST.get('memail')

        if MerchantDatabase.objects.filter(memail=memail).exists():
            messages.error(request,"Email Already Exists")
        else:
            MerchantDatabase.objects.create(mname=mname, mnumber=mnumber, memail=memail)
            return render(request, "merchant.html")
    else:
        return render(request,'merchant.html')

def display_merchant_data(request):
    mymerchantdata = MerchantDatabase.objects.all()
    result = {"data": mymerchantdata}
    return render(request, result)