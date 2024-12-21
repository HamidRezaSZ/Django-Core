from rest_framework import serializers

from base.models import City, State
from base.serializers.base_serializers import ModelSerializer


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = "__all__"


class StateItemSerializer(ModelSerializer):
    cities = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = "__all__"

    def get_cities(self, obj):
        return CitySerializer(obj.city_set.all(), many=True).data
