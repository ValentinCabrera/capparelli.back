from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from user.models import User
from rest_framework.authtoken.models import Token


class UserTokenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        mail = request.data.get("mail")
        password = request.data.get("password")

        user = get_object_or_404(User, mail=mail)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token":token.key})

        return Response({"error": "Usuario o contraseña incorrecta"})