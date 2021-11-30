from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.article import Article
from backend.serializers.article import ArticleSerializer


@extend_schema(
    description="Article's view description"
)
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
