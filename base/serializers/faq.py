from base.models import FAQ
from base.serializers.base_serializers import ModelSerializer


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
