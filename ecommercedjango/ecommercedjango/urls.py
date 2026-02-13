"""
URL configuration for ecommercedjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as v1
from terms import views as v2
from merchant import views as v3
from home import views as v4
from food import views as v5
from grocery import views as v6
from dineout import views as v7
from cart import views as  v8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',v1.login,name="login"),
    path('mydata/',v1.display_data),
    path('insert',v1.insert_data,name='insert_data'),
    path('terms/',v2.terms,name="terms"),
    path('merchant/',v3.merchant,name="merchant"),
    path('mymerchantdata/',v3.display_merchant_data),
    path('insertmerchantdata',v3.insert_merchant_data,name='insert_merchant_data'),
    path('',v4.home,name="home"),
    path('home/',v4.home,name='home'),
    path('food/',v5.food,name="food"),
    path('grocery/',v6.grocery,name="grocery"),
    path('dineout/',v7.dineout,name="dineout"),
    path('userlogin/',v1.userlogin,name="userlogin"),
    path('profile/',v1.profile,name='profile'),
    path('cart/',v8.cart,name="cart"),
]
