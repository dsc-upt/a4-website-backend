from rest_framework import viewsets

from backend.models.faqitem import FAQItem
from backend.serializers.faqitem import FAQItemSerializer


class FAQItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQItem.objects.all()
    serializer_class = FAQItemSerializer
