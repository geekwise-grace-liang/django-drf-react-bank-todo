from rest_framework import serializers
from .models import Branch, Customer
class Bank_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'bank_name', 'location',)
class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customer_name', 'phone_number', 'email', 'address',)