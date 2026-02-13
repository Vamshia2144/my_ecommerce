from django.shortcuts import render

# Create your views here.
def grocery(request):
    return render(request, 'grocery.html')