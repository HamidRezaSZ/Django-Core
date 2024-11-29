from accounts.models import Profile
from base.base_serializers import ModelSerializer
from base.serializers import CitySerializer


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user",)

    def update(self, instance, validated_data):
        user = self.context.get("user")
        validated_data["user"] = user

        return super().update(instance, validated_data)


class ProfileGetSerializer(ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Profile
        exclude = ("user",)
