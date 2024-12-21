from base.models import Slider
from base.serializers.base_serializers import ModelSerializer
from base.serializers.page import PageSerializer


class SliderSerializer(ModelSerializer):
    page = PageSerializer()

    class Meta:
        model = Slider
        exclude = ("order",)
