from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('email-step/', views.email_step, name='email_step'),
    path('payment-step/', views.payment_step, name='payment_step'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    

    
    
]