from django.shortcuts import render

# Create your views here.
from Customer_profile.models import Customer
from Customer_profile.serializer import CustomerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions


class CustomerViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions, ]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
