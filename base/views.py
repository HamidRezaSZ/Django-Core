from django.apps import apps
from django.core.exceptions import ValidationError
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


class ComponentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = ComponentGetSerializer
    queryset = Component.objects.filter(is_active=True, parent=None)
    filterset_fields = ['page__link', 'order', 'parent']


class ObjectInstanceView(CreateAPIView):
    serializer_class = ObjectInstanceSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = ObjectInstanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        app_name = serializer.data['app_name']
        model_name = serializer.data['model_name']
        object_id = serializer.data['object_id']
        quantity = serializer.data['quantity']
        try:
            model = apps.get_model(app_name, model_name)
        except LookupError:
            return Response({"message": f"No installed app with label '{app_name}'."}, status=404)
        obj = get_object_or_404(model, id=object_id)
        for _ in range(quantity):
            obj.pk = None
            obj.save()

        return Response({"message": "Objects created"}, status=200)
