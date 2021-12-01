from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.sponsor import Sponsor
from backend.serializers.sponsor import SponsorSerializer


@extend_schema(
    description="Sponsor's view description"
)
class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
