from back.utils.abm_urls import get_abm_patterns
from user.models import Client
from user.serializers import ClientSerializer

urlpatterns = get_abm_patterns(Client, ClientSerializer)