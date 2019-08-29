from rest_framework import serializers
from .models import Temperature,City,State
import ast

class CitySerializer(serializers.ModelSerializer):

    state=serializers.SerializerMethodField()

    class Meta:
        model=City
        fields=[
            'lat',
            'lng',
            'state',
            'name'
        ]
    def get_state(self,obj):
        return (obj.state.state)


class TemperatureSerializer(serializers.ModelSerializer):
    """
    serializers for getting list if blog categories
    """
    location = serializers.SerializerMethodField()
    temperature = serializers.SerializerMethodField()

    class Meta:
        model = Temperature
        fields = [
            'id',
            'location',
            'date',
            'temperature'
        ]

    def get_location(self, obj):
        locationserializer = CitySerializer(obj.city)

        return locationserializer.data

    def get_temperature(self, obj):

        return ast.literal_eval(obj.temperature)