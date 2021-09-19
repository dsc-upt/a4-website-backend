from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet
from backend.views.contact import ContactViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("contacts",ContactViewSet)

backend_urls = router.urls
