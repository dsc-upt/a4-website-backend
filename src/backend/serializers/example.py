from rest_framework import serializers

from backend.models.example import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        exclude = ('id',)
