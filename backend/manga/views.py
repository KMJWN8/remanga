from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import AgeRating, Category, Genre, MangaType, Status, Title
from .serializers import (
    AgeRatingSerializer,
    CategorySerializer,
    GenreSerializer,
    MangaTypeSerializer,
    StatusSerializer,
    TitleSerializer,
)


class AgeRatingViewSet(ReadOnlyModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MangaTypeViewSet(ReadOnlyModelViewSet):
    queryset = MangaType.objects.all()
    serializer_class = MangaTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StatusViewSet(ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
