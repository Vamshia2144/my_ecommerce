from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import EcommerceDatabase

def login(request):
    return render(request, 'login.html')

def insert_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #already exists
        if EcommerceDatabase.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered")
            return render(request, 'login.html')    
        elif EcommerceDatabase.objects.filter(number=number).exists():
            messages.error(request, "Mobile Number Already Registered")
            return render(request, 'login.html') 
        elif EcommerceDatabase.objects.filter(password=password).exists():
            messages.error(request, "Email Already Registered")
            return render(request, 'login.html')        
        else:
        # Insert Data into Database
            EcommerceDatabase.objects.create(name=name, number=number, email=email, password=password)
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')  # Redirect to login page

    return render(request, 'login.html')

def display_data(request):
    mydata = EcommerceDatabase.objects.all()
    result = {"data": mydata}
    return render(request, 'login.html', result)

def userlogin(request):
    if request.method == 'POST':
        usernumber = request.POST.get('lnumber')
        userpassword = request.POST.get('lpassword')
        try:
            user = EcommerceDatabase.objects.get(number=usernumber)
            if userpassword == user.password:
                request.session['user_pass'] = user.user_id
                request.session['user_name'] = user.name
                return redirect('profile')                 
            
            else:
                messages.error(request, "Incorrect Password")
        except:
            messages.error(request, "Number Not Exists")
    return render(request,'login.html')        
def profile(request):
    if 'user_pass' in request.session:
        name=request.session['user_name']
        return render(request,'home.html',{'name':name})
    return redirect('login')