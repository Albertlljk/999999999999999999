from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forests/', views.forests, name='forests'),
    path('oceans/', views.oceans, name='oceans'),
]
