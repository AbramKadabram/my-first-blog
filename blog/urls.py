from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('product/', views.shop_list, name='shop_list'),
    path('product/<int:pk>/', views.shop_detail, name='shop_detail'),
]