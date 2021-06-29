from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.example import Example
from backend.serializers.example import ExampleSerializer


@extend_schema(
    description="Some descriptions"
)
class ExampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
