from base.models import AboutUs
from base.serializers.base_serializers import ModelSerializer


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"
