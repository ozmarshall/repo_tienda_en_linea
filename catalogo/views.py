from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Articulo
from .serializers import ArticuloSerializer

import cloudinary.uploader

# Create your views here.

#lista general
class ArticuloApiView(generics.ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

#lista por id
class RetrieveArticulosView(generics.RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

#elimina por id
class DeleteArticuloView(generics.DestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

#edita por id
class UpdateArticuloView(generics.RetrieveUpdateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    
#envia datos 
class UploadArticuloImage(APIView):
    def post(self, request):
        file = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(file)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)


