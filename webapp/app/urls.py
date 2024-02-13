"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('' , views.home, name='home'),
    path('signout', views.signout, name='signout'),
    path('registerXlogin', views.registerXlogin, name='registerXlogin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('upload_profile_image/', upload_profile_image, name='upload_profile_image'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('admin1/', admin1, name='admin1'),
    path('management/', views.management, name='management'),
    path('user_management/', user_management_view, name='user_management'),
    path('products/', products, name='products'),
    path('product/<int:item_id>/', product, name='product'),
    path('productweb/product/<int:item_id>/', product, name='product'),
    path('contag/', contag, name='contag'),
    path('payments/', payments, name='payments'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('add_cart/<int:id>/', add_cart, name='add_cart'),
    path('cart/',cart,name='cart'),
    path('order',order,name='order'),
    path('order2',order2,name='order2'),
    path('order3',order3,name='order3'),
    path('order4',order4,name='order4'),
    path('order5',order5,name='order5'),
    path('order6',order6,name='order6'),
    path('preorder/', views.preorder, name='preorder'),
    path('orders/', views.admin_order_list, name='admin_order_list'),
    path('orders/', views.admin_order_list, name='admin_order_list'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('orders/view/<int:order_id>/', views.view_order, name='view_order'),
    path('orders/track/<int:order_id>/', views.track_order, name='track_order'),

]
