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


class ObjectInstanceView(CreateAPIView):
    serializer_class = ObjectInstanceSerializer
    permission_classes = (IsAdminUser,)

    def clone_object(self, obj, attrs={}):
        clone = obj._meta.model.objects.get(pk=obj.pk)
        clone.pk = None

        for key, value in attrs.items():
            setattr(clone, key, value)

        clone.save()

        fields = clone._meta.get_fields()
        for field in fields:
            if not field.auto_created and field.many_to_many:
                for row in getattr(obj, field.name).all():
                    getattr(clone, field.name).add(row)

            if field.auto_created and field.is_relation:
                if field.many_to_many:
                    pass
                else:
                    attrs = {
                        field.remote_field.name: clone
                    }
                    children = field.related_model.objects.filter(**{field.remote_field.name: obj})
                    for child in children:
                        self.clone_object(child, attrs)

        return clone

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

        try:
            for _ in range(quantity):
                self.clone_object(obj)

        except Exception as e:
            raise e

        return Response({"message": "Objects created"}, status=200)

    def get(self, request, *args, **kwargs):
        models = {}
        for model in apps.get_models():
            models[model.__name__] = model.__module__.split('.')[0]
        return Response({'models': models}, status=200)
