from rest_framework.routers import DefaultRouter

from backend.views.example import ExampleViewSet
from backend.views.contact import ContactViewSet
from backend.views.article import ArticleViewSet
from backend.views.faq import FaqViewSet
from backend.views.settings import SettingViewSet
from backend.views.menu import MenuViewSet
# from backend.views.project import ProjectViewSet
from backend.views.sponsor import SponsorViewSet
from backend.views.tag import TagViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)
router.register("contacts", ContactViewSet)
router.register("faqs", FaqViewSet)
router.register("settings", SettingViewSet)
router.register("articles", ArticleViewSet)
router.register("menu", MenuViewSet)
# router.register("projects", ProjectViewSet)
router.register("sponsor", SponsorViewSet)
router.register("tag", TagViewSet)

backend_urls = router.urls
