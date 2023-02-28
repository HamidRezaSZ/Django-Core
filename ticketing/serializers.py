from rest_framework import serializers

from base.base_serializers import ModelSerializer

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

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['client'] = user
        return super().create(validated_data)


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
        return TicketMessageSerializer(TicketMessage.objects.get(ticket=obj).message, many=True).data


class MessageFileSerializer(ModelSerializer):
    class Meta:
        model = MessageFile
        fields = '__all__'


class TicketMessageSerializer(ModelSerializer):
    files = serializers.SerializerMethodField()

    class Meta:
        model = TicketMessage
        fields = '__all__'

    def get_files(self, obj):
        return MessageFileSerializer(MessageFile.objects.get(message=obj).file, many=True).data


class CreateTicketMessageSerializer(ModelSerializer):
    files = MessageFileSerializer(many=True)

    class Meta:
        model = TicketMessage
        fields = '__all__'

    def create(self, validated_data):
        obj = super().create(validated_data)
        for file in validated_data['files']:
            MessageFile.objects.create(message=obj, file=file)

        return obj
