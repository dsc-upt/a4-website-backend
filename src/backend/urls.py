from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet

from backend.views.faq import FaqViewSet
from backend.views.settings import SettingViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("faqs", FaqViewSet)
router.register("settings", SettingViewSet)

backend_urls = router.urls
