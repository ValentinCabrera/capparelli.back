from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import ItemMenuSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ItemMenuSerializer()
    class Meta:
        model = OrderItem
        fields = ["quantity", "product"]

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "items", "subtotal", "total"]

    def get_items(self, order):
        items = order.items.all()

        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_subtotal(self, order):
        return order.get_subtotal()

    def get_total(self, order):
        return order.get_total()