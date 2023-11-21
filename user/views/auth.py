from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from user.models import User, MailCheck
from back.utils.mail import send_email


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

        if user.is_checked():
            token = user.log_in(password)

            if token:
                return Response({"token":token.key})

            else:
                return Response({"error": "Usuario o contraseña incorrecta."})

        else:
            user.send_mail()
            return Response({"error": "Porfavor, verifica el mail."})

class SignInView(APIView):
    def post(self, request):
        try:
            mail = request.data.get("mail")
            password = request.data.get("password")
            name = request.data.get("name")
            surname = request.data.get("surname")

            user = User(mail=mail, password=password, name=name, surname=surname)
            user.save()

        except:
            return Response({"error": "Error al crear el usuario."})

        try:
            mail_check = MailCheck(user=user)
            mail_check.save()

            return Response({"message": "Por favor, verifica el mail."})

        except:
            return Response({"error": "Error al enviar el mail de verificacion"})


class MailCheckView(APIView):
    def post(self, request):
        mail = request.data.get("mail")
        password = request.data.get("password")

        user = get_object_or_404(User, mail=mail)
        token = user.log_in(password)

        if token:
            if not user.is_checked():
                mail_token = request.data.get("token")
                mail_check = user.mail_check.first()

                if mail_check.check_token(mail_token):
                    return Response({"message": "Cuenta verificada con exito."})

                return Response({"error": "Error al verificar la cuenta."})

            return Response({"error": "No hay token para verificar."})

        else:
            return Response({"error": "Usuario o contraseña incorrecta."})