from rest_framework.serializers import ModelSerializer, SerializerMethodField

from base.models import Footer, FooterColumn, FooterImage, FooterRow, SocialAccount


class SocialAccountSerializer(ModelSerializer):
    class Meta:
        model = SocialAccount
        exclude = ("order",)


class FooterRowSerializer(ModelSerializer):
    class Meta:
        model = FooterRow
        exclude = ("order",)


class FooterColumnSerializer(ModelSerializer):
    rows = FooterRowSerializer(many=True)

    class Meta:
        model = FooterColumn
        exclude = ("order",)


class FooterImageSerializer(ModelSerializer):
    class Meta:
        model = FooterImage
        exclude = ("order",)


class FooterSerializer(ModelSerializer):
    images = SerializerMethodField()
    columns = SerializerMethodField()

    class Meta:
        model = Footer
        fields = "__all__"

    def get_images(self, footer: Footer):
        return FooterImageSerializer(FooterImage.active_objects.all(), many=True).data

    def get_columns(self, footer: Footer):
        return FooterColumnSerializer(FooterColumn.active_objects.all(), many=True).data
