from back.utils.abm_urls import get_abm_patterns
from user.models import Admin
from user.serializers import AdminSerializer

urlpatterns = get_abm_patterns(Admin, AdminSerializer)