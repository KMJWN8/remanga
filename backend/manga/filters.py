import django_filters

from .models import AgeRating, Category, Genre, MangaType, Status, Title


class TitleFilter(django_filters.FilterSet):
    type = django_filters.ModelMultipleChoiceFilter(
        queryset=MangaType.objects.all(),
        field_name="type",
        to_field_name="id",
    )

    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), field_name="categories", to_field_name="id"
    )

    genres = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        field_name="genres",
        to_field_name="id",
    )

    status = django_filters.ModelMultipleChoiceFilter(
        queryset=Status.objects.all(),
        field_name="status",
        to_field_name="id",
    )

    age_rating = django_filters.ModelMultipleChoiceFilter(
        queryset=AgeRating.objects.all(),
        field_name="age_rating",
        to_field_name="id",
    )

    rating_range = django_filters.RangeFilter(
        field_name="rating",
    )

    search = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Поиск по названию"
    )

    class Meta:
        model = Title
        fields = [
            "type",
            "categories",
            "genres",
            "status",
            "age_rating",
            "rating_range",
            "search",
        ]
