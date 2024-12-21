from base.models import Footer
from base.serializers.base_serializers import ModelSerializer
from base.serializers.contact_us import ContactUsDetailSerializer
from base.serializers.page import PageSerializer
from base.serializers.social_account import SocialAccountSerializer


class FooterSerializer(ModelSerializer):
    useful_link = PageSerializer(many=True)
    social_accounts = SocialAccountSerializer(many=True)
    contact_us = ContactUsDetailSerializer()

    class Meta:
        model = Footer
        fields = "__all__"
