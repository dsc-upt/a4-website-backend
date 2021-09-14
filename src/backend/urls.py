from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet
from backend.views.article import ArticleViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("articles", ArticleViewSet)

backend_urls = router.urls
