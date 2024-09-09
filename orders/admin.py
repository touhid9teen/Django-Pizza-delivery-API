from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_type', 'created_at', 'size', 'updated_at']
    list_filter = ['user', 'order_type', 'created_at', 'size', 'updated_at']