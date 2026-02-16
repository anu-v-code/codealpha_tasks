from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update-item/<int:pk>/<str:action>/', views.update_item, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),



]
