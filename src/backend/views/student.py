from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.student import Student
from backend.serializers.student import StudentSerializer


@extend_schema(
    description="Student's view description"
)
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
