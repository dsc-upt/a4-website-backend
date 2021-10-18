from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from django.conf import settings
from django.core.mail import send_mail

from backend.models.contact import Contact

from backend.serializers.contact import ContactSerializer


@extend_schema()
class ContactViewSet(viewsets.ReadOnlyModelViewSet, CreateModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        res = super(ContactViewSet, self).create(request, *args, **kwargs)
        if res.status_code == 201 and not settings.DEBUG:
            email = res.data["email"]
            subject = res.data["subject"]
            message = f"From: {res.data['name']}, {email}\n{res.data['message']}"
            send_mail(subject, message, None, ["mail1@mailinator.com"])
            send_mail("Submit Opportunity", "Îţi mulţumim că ne-ai contactat!", None, [email])
        if res.status_code == 201 and settings.DEBUG:
            print(f"From: {res.data['name']}, {res.data['email']}\n{res.data['message']}")
        return res