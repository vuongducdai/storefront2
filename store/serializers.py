from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='unit_price')
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'collection']

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal('1.1')