
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.pro_duct, name='product_catdetails'),



]
