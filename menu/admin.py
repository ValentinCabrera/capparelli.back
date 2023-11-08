from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CategoryDetail)
class CategoryDetailAdmin(admin.ModelAdmin):
    list_display = ['category', 'product']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(IngredientPrice)
class IngredientPriceAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'ingredient', 'price']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'product', 'price']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['product', 'ingredient', 'quantity']