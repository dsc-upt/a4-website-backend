from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet

from backend.views.faq import FaqViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("faqs", FaqViewSet)

backend_urls = router.urls
