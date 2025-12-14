from decimal import Decimal
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='unit_price')

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax']

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal('1.1')