from base.models import DynamicText
from base.serializers.base_serializers import ModelSerializer


class DynamicTextSerializer(ModelSerializer):
    class Meta:
        model = DynamicText
        fields = "__all__"
