from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.partner import Partner
from backend.serializers.partner import PartnerSerializer


@extend_schema(
    description="Partners' views description"
)

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
