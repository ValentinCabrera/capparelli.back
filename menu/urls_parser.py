"""from django.urls import path
from .views import *

app_name = 'pedidos'

urlpatterns = [
    path('crear/', CrearPedido.as_view()),
    path('agregar/', AgregarProducto.as_view()),
    path('cantidad/', ModificarCantidad.as_view()),
    path('confirmar/', ConfirmarPedido.as_view()),
]
"""

from django.urls import path, include
from .views import *

app_name = 'menu'

urlpatterns = [
    path('categories/', include('menu.urls.category')),
    path('products/', include('menu.urls.product')),
    path('menu/', include('menu.urls.menu'))
]