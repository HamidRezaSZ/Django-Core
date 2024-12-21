from base.models import SocialAccount
from base.serializers.base_serializers import ModelSerializer


class SocialAccountSerializer(ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = "__all__"
