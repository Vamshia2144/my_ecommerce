from django.shortcuts import render

# Create your views here.
def dineout(request):
    return render(request, 'dineout.html')