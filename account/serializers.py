from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
import stripe
stripe.api_key = "sk_test_51FnL8pBruBQCsvNc7zdb4wo41fuj0jFcCRWqLuT9e3RbngC4FEOGOhqXTN6iOFTv6QNVuQ2BBxQCghn0CrplE1gU00ZvXKxayp"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        Profile.objects.get_or_create(user=user)
        stripe.Customer.create(email=validated_data['email'])

        return user