from django.db import models
from menu.models import Product, Ingredient
from user.models import User

class OrderState(models.Model):
    name = models.CharField(max_length=50, unique=True)
    @classmethod
    def get_state(cls, name):
        states = ['pidiendo', 'preparando', 'listo']

        try:
            return OrderState.objects.get(name=name)

        except OrderState.DoesNotExist:
            if name in states:
                state = OrderState(name=name)
                state.save()
                return state

            raise ValueError(f"The state named {name} doestn exist.")

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')

    @classmethod
    def create_order(cls, client):
        orders = Order.objects.filter(client=client)

        for order in orders:
            if order.are_pidiendo():
                return order

        else:
            order = Order(client=client)
            order.save()
            order.create_state_change('pidiendo')
            return order

    def are_pidiendo(self):
        return self.states_change.last() == 'pidiendo'

    def are_preparando(self):
        return self.states_change.last() == 'preparando'
    def create_state_change(self, name):
        state = OrderState.get_state(name)
        change = OrderStateChange(state=state, order=self)
        change.save()

    def change_to_preparando(self):
        if self.items.all.count() > 0:
            self.create_state_change('preparando')

    def change_listo(self):
        self.create_state_change('listo')

class OrderStateChange(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    state = models.ForeignKey(OrderState, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='states_change')

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()

    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')

class ItemDetail(models.Model):
    quantity = models.PositiveIntegerField()

    order_item = models.ForeignKey(OrderItem, on_delete=models.RESTRICT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)