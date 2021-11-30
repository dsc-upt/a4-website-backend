from rest_framework import serializers
from backend.models.example import Project


class ProjectSerializer(serializers.ProjectSerializer):
    class Meta:
        model = Project
        fields = '__all__'
