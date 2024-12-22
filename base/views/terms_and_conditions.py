from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import TermsAndConditions
from base.serializers.terms_and_conditions import TermsAndConditionsSerializer
from base.views.viewsets import ModelViewSet


class TermsAndConditionsView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = TermsAndConditionsSerializer
    queryset = TermsAndConditions.objects.all()
