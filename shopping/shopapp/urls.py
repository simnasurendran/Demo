from django.contrib import admin
from django.urls import path

from shopping import settings
from . import views

app_name = 'shopapp'
urlpatterns = [

    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
