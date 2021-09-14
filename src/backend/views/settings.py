from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.settings import Setting

from backend.serializers.settings import SettingSerializer


@extend_schema(
    description="Some descriptions"
)
class SettingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
