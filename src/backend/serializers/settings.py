from rest_framework import serializers

from backend.models.settings import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
