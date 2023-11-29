from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']

@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ['order_item', 'ingredient', 'quantity']

@admin.register(OrderState)
class OrderStateAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(OrderStateChange)
class OrderStateChangeAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'order', 'state']

@admin.register(OrderDiscount)
class OrderDiscountAdmin(admin.ModelAdmin):
    list_display = ['order', 'discount']

@admin.register(DiscountCodePercentage)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'percentage']