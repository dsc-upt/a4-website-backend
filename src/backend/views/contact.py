from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from backend.models.contact import Contact

from backend.serializers.contact import ContactSerializer


@extend_schema()
class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer