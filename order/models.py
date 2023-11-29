from django.db import models
from menu.models import Product, Ingredient
from user.models import User

class OrderState(models.Model):
    name = models.CharField(max_length=50, unique=True)
    @classmethod
    def get_state(cls, name):
        states = ['pendiente', 'cocina', 'listo']

        try:
            return OrderState.objects.get(name=name)

        except OrderState.DoesNotExist:
            if name in states:
                state = OrderState(name=name)
                state.save()
                return state

            raise ValueError(f"The state named {name} doestn exist.")

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')

    @classmethod
    def get_or_create_order(self, client):
        order = client.get_actual_order()

        if order:
            return order

        order = Order(client=client)
        order.save()

        state = OrderState.get_state("pendiente")
        change = OrderStateChange(state=state, order=order)
        change.save()

        return order

    def __str__(self):
        return f"{self.pk} - {self.client}"

    def are_pendiente(self):
        return self.states_change.last().state.name == 'pendiente'

    def are_cocina(self):
        return self.states_change.last().state.name == 'cocina'

    def are_listo(self):
        return self.states_change.last().state.name == 'listo'
    def change_state(self, name):
        state = OrderState.get_state(name)
        change = OrderStateChange(state=state, order=self)
        change.save()

    def alter_item(self, product_id, quantity):
        try:
            item = self.items.get(product_id=product_id)
            item.quantity += quantity

            if item.quantity > 0:
                item.save()

            else:
                item.delete()

        except:
            if quantity > 0:
                item = OrderItem(product_id=product_id, order=self, quantity=quantity)
                item.save()

    def delete_item(self, product_id):
        item = self.items.filter(product_id=product_id)

        if item:
            item[0].delete()


    def get_subtotal(self):
        prices = map(lambda i: i.product.get_price() * i.quantity, self.items.all())
        return sum(prices)

    def get_total(self):
        total = self.get_subtotal()

        for i in self.discounts.all():
            total = i.discount.calculate(total)

        return total

class OrderStateChange(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    state = models.ForeignKey(OrderState, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='states_change')

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()

    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')

class ItemDetail(models.Model):
    quantity = models.PositiveIntegerField()

    order_item = models.ForeignKey(OrderItem, on_delete=models.RESTRICT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)

class DiscountStrategy(models.Model):
    class Meta:
        abstract = True
    def calculate(self, total):
        raise NotImplementedError("Método calculate debe ser implementado por las subclases")

class DiscountCodePercentage(DiscountStrategy):
    code = models.CharField(max_length=15)
    percentage = models.FloatField()

    def calculate(self, total):
        return total * (1 - self.percentage / 100)


class OrderDiscount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name="discounts")
    discount = models.ForeignKey(DiscountCodePercentage, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ("order", "discount")