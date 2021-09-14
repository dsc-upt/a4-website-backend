from rest_framework import serializers

from backend.models.faq import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
