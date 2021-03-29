import stripe
from django import setup
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

stripe.api_key = "sk_test_51FnL8pBruBQCsvNc7zdb4wo41fuj0jFcCRWqLuT9e3RbngC4FEOGOhqXTN6iOFTv6QNVuQ2BBxQCghn0CrplE1gU00ZvXKxayp"

## PAYMENT METHODS
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def payment_methods(request):
    payment_methods = stripe.PaymentMethod.list(customer=request.user.profile.stripe_id, type="card")
    return Response(payment_methods)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def payment_method_setup_token(request):
    setup_intent = stripe.SetupIntent.create(
        payment_method_types=["card"],
        customer = request.user.profile.stripe_id
    )
    return Response(setup_intent['client_secret'])

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_payment_method(request):
    stripe.PaymentMethod.detach(request.data['payment_method_id'])
    return Response(status=status.HTTP_200_OK)

## SUBSCRIPTIONS
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def subscription_plans(request):
    plans = stripe.Price.list(product='prod_JBC2GhbSt7X0Oc')
    return Response(plans)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_subscription(request):
    stripe.Subscription.create(
        customer=request.user.profile.stripe_id,
        items=[
            {
                "price": request.data['price'],
            },
        ],
        default_payment_method = request.data['default_payment_method']

    )
    return Response("Subscribed")
