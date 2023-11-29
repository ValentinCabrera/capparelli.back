from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer

class GetOrdersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        orders_cocina = list(filter(lambda i: i.are_cocina(), orders))
        orders_listo = list(filter(lambda i: i.are_listo(), orders))

        serializer_cocina = OrderSerializer(orders_cocina, many=True)
        serializer_listo = OrderSerializer(orders_listo, many=True)

        return Response({"cocina":serializer_cocina.data, "salon":serializer_listo.data})
