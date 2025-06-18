from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AgeRatingViewSet,
    CategoryViewSet,
    GenreViewSet,
    MangaTypeViewSet,
    StatusViewSet,
    TitleViewSet,
)

router = DefaultRouter()
router.register(r"titles", TitleViewSet)
router.register(r"age_ratings", AgeRatingViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"types", MangaTypeViewSet)
router.register(r"statuses", StatusViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
