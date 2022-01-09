from rest_framework import serializers
from Customer_profile.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields='__all__'
