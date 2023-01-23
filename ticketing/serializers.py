from rest_framework import serializers
from .models import *


class TicketSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('is_archive',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['client'] = user
        return super().create(validated_data)

    def get_status(self, obj):
        return StatusSerializer(TicketStatus.objects.get(ticket=obj).status).data

    def get_department(self, obj):
        return DepartmentSerializer(TicketDepartment.objects.get(ticket=obj).department).data

    def get_priority(self, obj):
        return PrioritySerializer(TicketPriority.objects.get(ticket=obj).priority).data


class TicketItemSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('is_archive',)

    def get_status(self, obj):
        return StatusSerializer(TicketStatus.objects.get(ticket=obj).status).data

    def get_department(self, obj):
        return DepartmentSerializer(TicketDepartment.objects.get(ticket=obj).department).data

    def get_priority(self, obj):
        return PrioritySerializer(TicketPriority.objects.get(ticket=obj).priority).data

    def get_messages(self, obj):
        return MessageSerializer(TicketMessage.objects.get(ticket=obj).message, many=True).data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_files(self, obj):
        return FileSerializer(MessageFile.objects.get(message=obj).file, many=True).data
