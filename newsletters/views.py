from base.viewsets import ModelViewSet
from .serializers import NewsLettersSerializer
from .models import NewsLetters
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class NewsLettersView(ModelViewSet):
    """
    Get email from user to register newsletters
    """

    serializer_class = NewsLettersSerializer
    queryset = NewsLetters.objects.all()
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
