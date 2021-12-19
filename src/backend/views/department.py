from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.department import Department
from backend.serializers.department import DepartmentSerializer


@extend_schema(
    description="Department's views description"
)

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
