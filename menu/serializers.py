from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ItemMenuSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def get_price(self, product):
        return product.get_price()

class MenuSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ["id", "name", "products"]

    def get_products(self, category):
        products = category.get_products()
        serializer = ItemMenuSerializer(products, many=True)

        return serializer.data
