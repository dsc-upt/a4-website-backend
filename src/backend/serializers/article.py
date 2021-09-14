from rest_framework import serializers

from backend.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('published',)
