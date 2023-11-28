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
    class Meta:
        model = Order
        fields = ["items"]

    def get_items(self, order):
        items = order.items.all()

        serializer = OrderItemSerializer(items, many=True)
        return serializer.data