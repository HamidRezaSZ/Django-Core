from base.serializers.base_serializers import ModelSerializer

from .models import NewsLetters


class NewsLettersSerializer(ModelSerializer):
    class Meta:
        model = NewsLetters
        fields = '__all__'
