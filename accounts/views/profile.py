from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from accounts.models import Profile
from accounts.serializers.profile import ProfileGetSerializer, ProfileSerializer
from base.viewsets import ModelViewSet


class ProfileView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ProfileGetSerializer

        return ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
