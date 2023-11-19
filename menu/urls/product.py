from .partials import get_abm_patterns
from menu.models import Product
from menu.serializers import ProductSerializer

urlpatterns = get_abm_patterns(Product, ProductSerializer)