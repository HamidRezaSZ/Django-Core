from django.apps import apps
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import Response

from .models import FAQ, AboutUs, ContactUsDetail, ContactUsForm
from .serializers import *
from .viewsets import ModelViewSet


class FAQView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    serializer_class = FAQSerializer
    queryset = FAQ.objects.filter(is_active=True)


class AboutUsView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.filter(is_active=True)


class ContactUsFormView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [AllowAny],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = ContactUsFormSerializer
    queryset = ContactUsForm.objects.all()


class ContactUsDetailView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ContactUsDetail.objects.filter(is_active=True)
    serializer_class = ContactUsDetailSerializer


class MenuView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Menu.objects.filter(is_active=True, parent=None)
    serializer_class = MenuGetSerializer


class SliderView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
    filterset_fields = ['page__link', 'page']


class FooterView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Footer.objects.filter(is_active=True)
    serializer_class = FooterSerializer


class CityView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer
    filterset_fields = ['state']


class StateView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = State.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StateItemSerializer

        return StateSerializer


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
    queryset = TermsAndConditions.objects.filter(is_active=True)


class DynamicTextView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = DynamicTextSerializer
    queryset = DynamicText.objects.filter(is_active=True)
