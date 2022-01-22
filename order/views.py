from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from .models import OrderItem
from .serializers import *  


@api_view(['GET', 'POST'])
def order_item(request):
    """
    List all order items, or create a new order item.
    """
    if request.method == 'GET':
        orders = OrderItem.objects.all()
        serializer = OrderItemSerializer(orders,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        print(data, 'yii')
        print(type(data), 'yii')
        data['total_price'] = data['totalPrice']
        data['qty'] = data['count']
        data['product'] = data['id']
        serializer = OrderItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
