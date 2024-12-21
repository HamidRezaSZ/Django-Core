from base.models import ContactUsDetail, ContactUsForm
from base.serializers.base_serializers import ModelSerializer
from base.serializers.social_account import SocialAccountSerializer


class ContactUsFormSerializer(ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = "__all__"


class ContactUsDetailSerializer(ModelSerializer):
    social_accounts = SocialAccountSerializer(many=True)

    class Meta:
        model = ContactUsDetail
        fields = "__all__"
