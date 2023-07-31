
from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.addtocart, name='addtocart'),
    path('minus/', views.minus, name='minus'),
    path('plus/', views.plus, name='plus'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pay/', views.paymentMethodSelected, name='paymentMethodSelected'),
    path('pay-with-stripe/', views.payWithStripe, name='payWithStripe'),
    path('pay-with-stripe-confirmation', views.payWithStripeConfirmation, name='payWithStripeConfirmation'),
    
    path('<str:pk>/', views.shopd, name='shopd'),
] 
