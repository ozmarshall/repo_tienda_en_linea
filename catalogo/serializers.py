from rest_framework import serializers
from .models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        return representation