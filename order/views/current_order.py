from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from order.models import Order, DiscountCodePercentage, OrderDiscount
from order.serializers import OrderSerializer

class GetOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        order = Order.get_or_create_order(user)

        serializer = OrderSerializer(order)
        return Response(serializer.data)

class AddItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order = Order.get_or_create_order(user)

        product_id = request.data.get("product")
        quantity = request.data.get("quantity")
        order.alter_item(product_id, quantity)

        serializer = OrderSerializer(order)

        return Response(serializer.data)

class AddDiscountView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order = Order.get_or_create_order(user)

        code = request.data.get("code")
        discount = get_object_or_404(DiscountCodePercentage, code=code)

        order_discount, created = OrderDiscount.objects.get_or_create(order=order, discount=discount)

        serializer = OrderSerializer(order)
        return Response(serializer.data)

class DeleteItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        order = Order.get_or_create_order(user)

        product_id = request.data.get("product")
        order.delete_item(product_id)

        serializer = OrderSerializer(order)

        return Response(serializer.data)

class OrderToKitchenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        order = Order.get_or_create_order(user)

        if order.items.count() > 0:
            order.change_state("cocina")

        serializer = OrderSerializer(order)

        return Response(serializer.data)