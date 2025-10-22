from django.contrib import admin 
from django.urls import path, include
from django.shortcuts import render


def home(request): return render(request, 'x1x1x1/home.html')
def forests(request): return render(request, 'x1x1x1/forests.html')
def oceans(request): return render(request, 'x1x1x1/oceans.html')


urlpatterns = [ path('admin/', admin.site.urls), 
               path('', include('x1x1x1.urls'))]