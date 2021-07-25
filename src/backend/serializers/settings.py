from rest_framework import serializers

from backend.models.settings import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        exclude = ('id',)
