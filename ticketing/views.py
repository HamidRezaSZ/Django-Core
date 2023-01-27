from base.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404


class TicketView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    filterset_fields = ['created_date', 'modified_date', 'is_archive', 'status', 'department', 'priority']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TicketItemSerializer

        return TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(client=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Ticket, client=self.request.user, pk=pk)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context


class DepartmentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = TicketDepartment.objects.filter(is_active=True)
    serializer_class = TicketDepartmentSerializer


class PriorityView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = TicketPriority.objects.filter(is_active=True)
    serializer_class = TicketPrioritySerializer


class StatusView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = TicketStatus.objects.filter(is_active=True)
    serializer_class = TicketStatusSerializer


class TicketMessageView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = TicketMessage.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTicketMessageSerializer

        return TicketMessageSerializer
