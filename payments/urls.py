from django.urls import path
from . import views

urlpatterns = [
    path('payment-methods/', views.payment_methods),
    path('payment-methods/setup-token/', views.payment_method_setup_token),
    path('payment-methods/delete/', views.delete_payment_method),

    path('subscriptions/', views.subscription_plans),
    path('subscriptions/create/', views.create_subscription),

]
