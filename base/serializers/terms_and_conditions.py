from base.models import TermsAndConditions
from base.serializers.base_serializers import ModelSerializer


class TermsAndConditionsSerializer(ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = "__all__"
