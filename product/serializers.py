from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product 
        fields = ('id', 'active', 'title', 'category', 'qty', 'price', 'image_path',)
  