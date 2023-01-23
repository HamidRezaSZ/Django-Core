from rest_framework import serializers
from .models import NewsLetters


class NewsLettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetters
        fields = '__all__'
