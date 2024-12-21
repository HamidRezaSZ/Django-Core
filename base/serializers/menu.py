from base.models import Menu
from base.serializers.base_serializers import ModelSerializer, RecursiveField
from base.serializers.page import PageSerializer


class MenuSerializer(ModelSerializer):
    page = PageSerializer()
    children = RecursiveField(many=True)

    class Meta:
        model = Menu
        exclude = ("parent",)
