from products.serializers import ProductSerializer
from .models import Bill
from rest_framework import serializers
    

class BillSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model  = Bill
        fields = ['id','client_id', 'company_name', 'nit', 'code', 'products', 'is_active']