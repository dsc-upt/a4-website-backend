from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet

from backend.views.faqitem import FAQItemViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("faqs", FAQItemViewSet)

backend_urls = router.urls
