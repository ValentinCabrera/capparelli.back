from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from back.utils.abm_utils import active
from menu.models import Category
from menu.serializers import MenuSerializer

class MenuView(APIView):
    def get(self, request):
        categories = active(Category)
        serializer = MenuSerializer(categories, many=True)

        return Response(serializer.data)

