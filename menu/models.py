from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    state = models.BooleanField(default=True)

    @classmethod
    def get_active_categories(cls):
        return Category.objects.filter(state=False)

    def __str__(self):
        return self.name

    def get_products(self):
        return self.products.filter(product__state=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    state = models.BooleanField(default=True)

    product = models.ForeignKey("self", on_delete=models.RESTRICT, blank=True, null=True, related_name="variants")

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    date_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='prices')


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    stock = models.FloatField()

    def __str__(self):
        return self.name


class IngredientPrice(models.Model):
    date_time = models.DateTimeField()
    price = models.PositiveIntegerField()

    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT, related_name='prices')


class Recipe(models.Model):
    quantity = models.FloatField()

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)


class CategoryDetail(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='categories')
