from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .filters import TitleFilter
from .models import (
    AgeRating,
    Category,
    Genre,
    MangaType,
    Status,
    Title,
    CustomUser,
)
from .serializers import (
    AgeRatingSerializer,
    CategorySerializer,
    GenreSerializer,
    MangaTypeSerializer,
    StatusSerializer,
    TitleSerializer,
    UserSerializer,
)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
