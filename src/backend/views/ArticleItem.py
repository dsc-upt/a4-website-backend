from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.ArticleItem import ArticleItem
from backend.serializers.ArticleItem import ArticleItemSerializer


@extend_schema(
    description="ArticleItem's view description"
)
class ArticleItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleItem.objects.all()
    serializer_class = ArticleItemSerializer