from rest_framework import serializers

from backend.models.ArticleItem import ArticleItem


class ArticleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleItem
        #name = serializers.CharField(max_length=100)
        #content = serializers.TextField()
        exclude = ('id',)
