from base.models import Page
from base.serializers.base_serializers import ModelSerializer


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
