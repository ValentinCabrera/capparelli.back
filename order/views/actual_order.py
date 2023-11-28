from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
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


