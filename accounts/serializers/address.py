from accounts.models import Address
from base.serializers.base_serializers import ModelSerializer
from base.serializers.state import CitySerializer


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ("user",)

    def create(self, validated_data):
        user = self.context.get("user")
        validated_data["user"] = user
        return super().create(validated_data)


class AddressGetSerializer(ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        exclude = ("user",)
