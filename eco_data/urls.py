from django.urls import path
from . import views



urlpatterns =[
    path('', views.endpoint, name='endpoint'),
    path('users/', views.users, name='users'),
    path('products/', views.products, name='products'),
    path('product/<str:product_id>/', views.product, name='product'),
    # path('users/', views.users, name='users'),
]