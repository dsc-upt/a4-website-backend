from rest_framework import serializers


class FAQItemSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=500)
    answer = serializers.CharField(max_length=500)
    publish_date = serializers.DateField()
