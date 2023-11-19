from .partials import get_abm_patterns
from menu.models import Category
from menu.serializers import CategorySerializer

urlpatterns = get_abm_patterns(Category, CategorySerializer)