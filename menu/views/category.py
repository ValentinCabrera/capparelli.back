from menu.models import Category
from menu.serializers import CategorySerializer
from back.utils import Active, Inactive, Delete, Recover, New, Alter

class Alter(Alter):
    Model = Category
    Serializer = CategorySerializer

class Active(Active):
    Model = Category
    Serializer = CategorySerializer

class Inactive(Inactive):
    Model = Category
    Serializer = CategorySerializer

class Delete(Delete):
    Model = Category
    Serializer = CategorySerializer

class Recover(Recover):
    Model = Category
    Serializer = CategorySerializer

class New(New):
    Model = Category
    Serializer = CategorySerializer