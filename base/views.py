from .serializers import *
from .models import FAQ, AboutUs, ContactUsDetail, ContactUsForm
from .viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny


class FAQView(ModelViewSet):
    """
    Get list of FAQs
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    serializer_class = FAQSerializer
    queryset = FAQ.objects.filter(is_active=True)


class AboutUsView(ModelViewSet):
    """
    Get about us page
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.filter(is_active=True)


class ContactUsFormView(ModelViewSet):
    """
    Create contact us form
    """

    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "post": [AllowAny],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = ContactUsFormSerializer
    queryset = ContactUsForm.objects.all()


class ContactUsDetailView(ModelViewSet):
    """
    Get contact us page
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ContactUsDetail.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return ContactUsGetDetailSerializer

        return ContactUsDetailSerializer


class MenuView(ModelViewSet):
    """
    Get menu list
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Menu.objects.filter(is_active=True, parent=None)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return MenuGetSerializer

        return MenuSerializer


class SliderView(ModelViewSet):
    """
    Get slider list
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer


class FooterView(ModelViewSet):
    """
    Get footer
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Footer.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return FooterGetSerializer

        return FooterSerializer


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

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return CityGetSerializer

        return CitySerializer


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
    """
    Get terms and conditions page
    """

    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = TermsAndConditionsSerializer
    queryset = TermsAndConditions.objects.filter(is_active=True)
