from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.menu import Menu
from backend.serializers.menu import MenuSerializer


@extend_schema(
    description="Some descriptions"
)
class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
