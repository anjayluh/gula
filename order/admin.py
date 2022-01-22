from django.contrib import admin

from .models import OrderItem
from .forms import OrderItemForm

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'qty', 'total_price',]
    list_select_related = ['product',]
    list_filter = ['product', 'qty', ]
    list_per_page = 50
    fields = ['product', 'qty', 'total_price',]
    read_only_fields = ['total_price']
    form = OrderItemForm