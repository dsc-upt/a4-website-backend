from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.tag import Tag
from backend.serializers.tag import TagSerializer


@extend_schema(
    description="Tag's view description"
)
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

##please work