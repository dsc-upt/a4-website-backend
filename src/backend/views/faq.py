from rest_framework import viewsets

from backend.models.faq import Faq
from backend.serializers.faq import FaqSerializer


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
