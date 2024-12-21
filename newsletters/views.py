from rest_framework.permissions import AllowAny, IsAdminUser

from base.views.viewsets import ModelViewSet

from .models import NewsLetters
from .serializers import NewsLettersSerializer


class NewsLettersView(ModelViewSet):
    """
    Get email from user to register newsletters
    """

    serializer_class = NewsLettersSerializer
    queryset = NewsLetters.objects.all()
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [AllowAny],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
