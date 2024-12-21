from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from base.serializers.base_serializers import ModelSerializer

from .models import *


class TicketDepartmentSerializer(ModelSerializer):
    class Meta:
        model = TicketDepartment
        fields = '__all__'


class TicketPrioritySerializer(ModelSerializer):
    class Meta:
        model = TicketPriority
        fields = '__all__'


class TicketStatusSerializer(ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    status = TicketStatusSerializer()
    department = TicketDepartmentSerializer()
    priority = TicketPrioritySerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('is_archive', 'status')


class TicketMessageSerializer(ModelSerializer):
    files = serializers.SerializerMethodField()

    class Meta:
        model = TicketMessage
        exclude = ('ticket',)
        read_only_fields = ('user',)

    def get_files(self, obj):
        return MessageFileSerializer(MessageFile.objects.get(message=obj).file, many=True).data


class TicketItemSerializer(ModelSerializer):
    status = TicketStatusSerializer()
    department = TicketDepartmentSerializer()
    priority = TicketPrioritySerializer()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('is_archive', 'status')

    def get_messages(self, obj):
        return TicketMessageSerializer(obj.ticketmessage_set.all(), many=True).data


class CreateTicketSerializer(ModelSerializer):
    message = TicketMessageSerializer(write_only=True)

    class Meta:
        model = Ticket
        exclude = ('client',)
        read_only_fields = ('status',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['client'] = user
        message = validated_data.pop('message')
        obj = super().create(validated_data)
        for msg in message:
            TicketMessage.objects.create(
                ticket=obj, user=user, content=msg)
        return obj


class MessageFileSerializer(ModelSerializer):
    class Meta:
        model = MessageFile
        exclude = ('message',)


class CreateTicketMessageSerializer(ModelSerializer):
    files = MessageFileSerializer(
        many=True, required=False, write_only=True)

    class Meta:
        model = TicketMessage
        exclude = ('user',)

    def validate(self, attrs):
        if attrs['ticket'].status.title == 'closed':
            raise serializers.ValidationError(_('The ticket is closed.'))

        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user

        files = []
        if validated_data.get('files'):
            files = validated_data.pop('files')

        obj = super().create(validated_data)
        for file in files:
            MessageFile.objects.create(message=obj, file=file)

        return obj
