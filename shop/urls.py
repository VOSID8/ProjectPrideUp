from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('shop/', views.shop, name='shop_homepage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.events, name='events'),
    path('product/<slug:slug>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('orders/', views.order, name="orders"),
    path('about/', views.about, name="about"),
    path('support/', views.support, name="support"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name="signup"),
    path('remove-cart-item/', views.removeCartItem, name="remove_cart_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('menu/', views.menu, name="menu"),
]