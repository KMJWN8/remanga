import django_filters

from .models import Title


class TitleFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(field_name="type")
    categories = django_filters.CharFilter(field_name="categories")
    genres = django_filters.CharFilter(field_name="genres")
    status = django_filters.CharFilter(field_name="status")

    class Meta:
        model = Title
        fields = ["type", "categories", "genres", "status"]
