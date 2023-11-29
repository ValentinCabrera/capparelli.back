from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from order.models import Order
from order.serializers import OrderSerializer


class FinishOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get("order")

        order = get_object_or_404(Order, id=order_id)
        order.change_state("listo")

        serializer = OrderSerializer(order)
        return Response(serializer.data)

class GetOrdersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        orders = list(filter(lambda i: i.are_cocina(), orders))
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)
