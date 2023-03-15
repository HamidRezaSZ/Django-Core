from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .base_serializers import ModelSerializer
from .models import *


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactUsFormSerializer(ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = '__all__'


class SocialAccountSerializer(ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = '__all__'


class ContactUsDetailSerializer(ModelSerializer):
    social_accounts = SocialAccountSerializer()

    class Meta:
        model = ContactUsDetail
        fields = '__all__'


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    page = PageSerializer()

    class Meta:
        model = Menu
        fields = '__all__'


class MenuGetSerializer(ModelSerializer):
    page = PageSerializer()
    sub_menus = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        exclude = ('parent',)

    def get_sub_menus(self, obj):
        return MenuSerializer(obj.children.all(), many=True, read_only=True).data


class SliderSerializer(ModelSerializer):
    page = PageSerializer()

    class Meta:
        model = Slider
        exclude = ('order',)


class FooterSerializer(ModelSerializer):
    useful_link = PageSerializer(many=True)
    social_accounts = SocialAccountSerializer(many=True)
    contact_us = ContactUsDetailSerializer()

    class Meta:
        model = Footer
        fields = '__all__'


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = '__all__'


class StateItemSerializer(ModelSerializer):
    cities = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = '__all__'

    def get_cities(self, obj):
        return CitySerializer(obj.city_set.all(), many=True).data


class TermsAndConditionsSerializer(ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'


class ComponentItemSerializer(ModelSerializer):
    class Meta:
        model = ComponentItem
        fields = '__all__'


class ComponentSerializer(ModelSerializer):
    page = PageSerializer(many=True)
    items = serializers.SerializerMethodField()

    class Meta:
        model = Component
        exclude = ('parent',)

    def get_items(self, obj):
        return ComponentItemSerializer(obj.componentitem_set.filter(is_active=True), many=True).data


class ComponentGetSerializer(ModelSerializer):
    page = PageSerializer(many=True)
    sub_component = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Component
        exclude = ('parent',)

    def get_sub_component(self, obj):
        return ComponentSerializer(obj.children.all(), many=True, read_only=True).data

    def get_items(self, obj):
        return ComponentItemSerializer(obj.componentitem_set.filter(is_active=True), many=True).data


class ObjectInstanceSerializer(serializers.Serializer):
    app_name = serializers.CharField()
    model_name = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1)
    object_id = serializers.IntegerField(min_value=1)
