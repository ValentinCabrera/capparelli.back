from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category
from .serializers import CategorySerializer

class GetCategories(APIView):
    def get(self, request):
        categories = Category.get_active_categories()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)