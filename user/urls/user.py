from back.utils.abm_urls import get_abm_patterns
from user.models import User
from user.serializers import UserSerializer

urlpatterns = get_abm_patterns(User, UserSerializer)