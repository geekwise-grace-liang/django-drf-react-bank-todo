from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Bank_Serializer, Customer_Serializer
from .models import Branch, Customer

# Create your views here.
class BranchView(viewsets.ModelViewSet):
    serializer_class = Bank_Serializer
    queryset = Branch.objects.all()
    
class CustomerView(viewsets.ModelViewSet):
    serializer_class = Customer_Serializer
    queryset = Customer.objects.all()