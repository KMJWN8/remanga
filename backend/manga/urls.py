from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AgeRatingViewSet,
    CategoryViewSet,
    GenreViewSet,
    MangaTypeViewSet,
    StatusViewSet,
    TitleViewSet,
    UserViewSet,
    UserProfileView,
)

router = DefaultRouter()
router.register(r"titles", TitleViewSet)
router.register(r"age_ratings", AgeRatingViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"types", MangaTypeViewSet)
router.register(r"statuses", StatusViewSet)

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
]
