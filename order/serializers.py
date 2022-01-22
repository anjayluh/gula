from .models import OrderItem
from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem 
        fields = ('product', 'qty', 'total_price',)
  