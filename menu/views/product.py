from menu.models import Product
from menu.serializers import ProductSerializer
from back.utils import Active, Inactive, Delete, Recover, New, Alter

class Alter(Alter):
    Model = Product
    Serializer = ProductSerializer

class Active(Active):
    Model = Product
    Serializer = ProductSerializer

class Inactive(Inactive):
    Model = Product
    Serializer = ProductSerializer

class Delete(Delete):
    Model = Product
    Serializer = ProductSerializer

class Recover(Recover):
    Model = Product
    Serializer = ProductSerializer

class New(New):
    Model = Product
    Serializer = ProductSerializer