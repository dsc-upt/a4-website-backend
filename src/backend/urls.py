from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet
from backend.views.ArticleItem import ArticleItemViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("ArticleItems", ArticleItemViewSet)

backend_urls = router.urls
