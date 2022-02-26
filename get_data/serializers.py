from rest_framework import serializers
from .models import Providers, Polygons


class ProviderSerializer(serializers.ModelSerializer):
    """
    This is the serializer for the Providers model.
    """
    class Meta:
        model = Providers
        fields = ('name', 'email', 'phone_number', 'language', 'currency')


class PolygonSerializer(serializers.ModelSerializer):
    """
    This is the serializer for the Polygons model.
    """
    class Meta:
        model = Polygons
        geo_field = "service_area"
        fields = '__all__'