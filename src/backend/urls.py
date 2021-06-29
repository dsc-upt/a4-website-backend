from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)

backend_urls = router.urls
