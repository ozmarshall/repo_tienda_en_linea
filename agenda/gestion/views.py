from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from .serializer import PruebaSerializer, TareaSerializer, EtiquetaSerializer, TareasSerializer, TareaPersonalizableSerializer, ArchivoSerializer, EliminarArchivoSerializer
from.models import Tareas, Etiqueta, Tareas
from rest_framework import status
#from datetime import datetime
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import remove
from django.conf import settings


@api_view(http_method_names=['GET', 'POST'])
def inicio(request):

    print(request.method)
    print(request)
    if request.method == 'GET':
        return Response(data={

            'messages': 'Bienvenido a mi Api dew Agenda'
        })

    elif request.method == 'POST':

        return Response(data={
            'messages': 'Hicciste un post'
        }, status=201)


class PruebaApiView(ListAPIView):
    serializer_class = PruebaSerializer
    queryset = [

        {
            'nombre': 'Pedro',
            'apellido': 'Ram',
            'correo': 'parc.tec20@yahoo.com',
            'dni': '22222222',
            'estado_civil': 'soltero'
        },

        {
            'nombre': 'juan',
            'apellido': 'Perez',
            'correo': 'perez@yahoo.com',
            'dni': '22222222',
            'estado_civil': 'soltero'
        }

    ]

    def get(self, request: Request):

        informacion = self.queryset
        informacion_serializada = self.serializer_class(
            data=informacion, many=True)
        informacion_serializada.is_valid(raise_exception=True)

        return Response(data={
            'message': 'Hola',
            'content': informacion_serializada.data
        })


class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def post(self, request: Request):
        serializador=self.serializer_class(data=request.data)

        if serializador.is_valid():
            fechasCaducidad=serializador.validated_data.get('fechasCaducidad')
            print(type(serializador.validated_data.get('fechasCaducidad')))
            importancia=serializador.validated_data.get('importancia')
            if importancia <0 or importancia >10:
                return Response(data={
                    'message': 'La importancia puede ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            if timezone.now() > fechasCaducidad: 
                return Response(data={
                    'message': 'La fecha no puede ser menor que la fecha actual'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializador.save()


            return Response(data=serializador.data, status=status.HTTP_201_CREATED)
        else:
            #serializador.errors
            return Response(data= {'message':'La data no es valida',
                                 'content': serializador.errors},
                                  status=status.HTTP_400_BAD_REQUEST)
 
       

class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer



class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class= TareaSerializer
    queryset= Tareas.objects.all()

class ArchivosApiView(CreateAPIView):
    serializer_class= ArchivoSerializer

    def post(self, request: Request):
        print(request.FILES)

        queryParams = request.query_params
        carpetaDestino = queryParams.get('carpeta')


        data=self.serializer_class(data= request.FILES)
        if data.is_valid():
            print(type(data.validated_data.get('archivo')))
            archivo: InMemoryUploadedFile= data.validated_data.get('archivo')
            #print(archivo.name)
            print(archivo.size)

            if archivo.size > (5 * 1024 * 1024):
                return Response(data={
                    'message': 'Archivo muy grabde , no pyuede ser nmas de 5 mb'
                }, status=status.HTTP_400_BAD_REQUEST)

            resultado=default_storage.save((carpetaDestino+'/' if carpetaDestino is not None else '')+archivo.name, ContentFile(archivo.read()))


            print(resultado)
            return Response(data={
                'message': 'Archivo guardado exitsamente',
                'content': {
                    'ubicacion': resultado
                    
                }

            }, status=status.HTTP_201_CREATED)

          
        else:
            return Response(data={
                'message': 'Error al subir imagen',
                'content': data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class EliminarArchivoApiView(DestroyAPIView):

    serializer_class = EliminarArchivoSerializer
    def delete(self, request: Request):
        data = self.serializer_class(data= request.data)
        try:

            data.is_valid(raise_exception=True)
            ubicacion = data.validated_data.get('archivo')
            remove(settings.MEDIA_ROOT/ ubicacion)
            return Response(data={
                'message': 'Archivo eliminado correctamente'
            })


           
        except Exception as e:
            return Response(data={
                'message': 'no se encontro el archivo a eliminar',
                'content': e.args

            }, status=status.HTTP_404_NOT_FOUND)


       