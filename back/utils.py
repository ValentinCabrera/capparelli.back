from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

def recover(entity):
    entity.state = True
    entity.save()


def delete(entity):
    entity.state = False
    entity.save()


def active(Model):
    return Model.objects.filter(state=True)


def inactive(Model):
    return Model.objects.filter(state=False)


class Alter(APIView):
    Model = None
    Serializer = None

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


class New(APIView):
    Model = None
    Serializer = None

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


class Active(APIView):
    Model = None
    Serializer = None

    def get(self, request):
        entities = active(self.Model)
        serializer = self.Serializer(entities, many=True)

        return Response(serializer.data)


class Inactive(APIView):
    Model = None
    Serializer = None

    def get(self, request):
        entities = inactive(self.Model)
        serializer = self.Serializer(entities, many=True)

        return Response(serializer.data)


class Delete(APIView):
    Model = None
    Serializer = None

    def post(self, request):
        id = request.data.get("id")
        entity = get_object_or_404(self.Model, id=id)
        delete(entity)
        serializer = self.Serializer(entity)

        return Response(serializer.data)


class Recover(APIView):
    Model = None
    Serializer = None

    def post(self, requst):
        id = requst.data.get("id")
        entity = get_object_or_404(self.Model, id=id)
        recover(entity)
        serializer = self.Serializer(entity)

        return Response(serializer.data)
