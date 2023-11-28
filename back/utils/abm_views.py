from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdmin
from .abm_utils import recover, delete, active, inactive

class AlterView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        id = request.data.get("id")
        instance = get_object_or_404(self.Model, id=id)

        try:
            for attr, value in request.data.items():
                if attr != 'id':
                    setattr(instance, attr, value)

            instance.save()

            serializer = self.Serializer(instance)
            return Response(serializer.data)

        except IntegrityError:
            return Response({'error': f'Uno de los atributos ya existe en otra fila.'})

        except Exception as e:
            return Response({'error': e})

class NewView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        try:
            instance = self.Model(**request.data)
            instance.save()

            serializer = self.Serializer(instance)
            return Response(serializer.data)

        except IntegrityError:
            return Response({'error': f'Uno de los atributos ya existe en otra fila.'})

        except Exception as e:
            return Response({"error": str(e)})

class ActiveView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        entities = active(self.Model)
        serializer = self.Serializer(entities, many=True)

        return Response(serializer.data)

class InactiveView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        entities = inactive(self.Model)
        serializer = self.Serializer(entities, many=True)
        self.as_view()

        return Response(serializer.data)

class DeleteView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        id = request.data.get("id")
        entity = get_object_or_404(self.Model, id=id)
        delete(entity)
        serializer = self.Serializer(entity)

        return Response(serializer.data)

class RecoverView(APIView):
    Model = None
    Serializer = None

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, requst):
        id = requst.data.get("id")
        entity = get_object_or_404(self.Model, id=id)
        recover(entity)
        serializer = self.Serializer(entity)

        return Response(serializer.data)

def get_active_view(model, serializer):
    class Active(ActiveView):
        Model = model
        Serializer = serializer

    return Active

def get_inactive_view(model, serializer):
    class Inactive(InactiveView):
        Model = model
        Serializer = serializer

    return Inactive

def get_delete_view(model, serializer):
    class Delete(DeleteView):
        Model = model
        Serializer = serializer

    return Delete

def get_recover_view(model, serializer):
    class Recover(RecoverView):
        Model = model
        Serializer = serializer

    return Recover

def get_new_view(model, serializer):
    class New(NewView):
        Model = model
        Serializer = serializer

    return New

def get_alter_view(model, serializer):
    class Alter(AlterView):
        Model = model
        Serializer = serializer

    return Alter