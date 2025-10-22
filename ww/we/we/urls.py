from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ path('admin/', admin.site.urls), 
               path('', include('x1x1x1.urls'))]