from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from .models import (
    AgeRating,
    Category,
    Genre,
    MangaType,
    Status,
    Title,
    CustomUser,
)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ["id", "email", "username", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "username", "first_name", "last_name"]


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MangaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaType
        fields = ["id", "name"]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]


class TitleSerializer(serializers.ModelSerializer):
    type = MangaTypeSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    age_rating = AgeRatingSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Title
        fields = [
            "id",
            "name",
            "alt_name",
            "description",
            "cover",
            "type",
            "categories",
            "genres",
            "status",
            "rating",
            "age_rating",
            "year_released",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        request = self.context.get("request")

        type_id = request.data.get("type")
        age_rating_id = request.data.get("age_rating")
        status_id = request.data.get("status")
        category_ids = request.data.get("categories", [])
        genre_ids = request.data.get("genres", [])

        # Получаем связанные объекты или устанавливаем None
        manga_type = self._get_instance_or_none(MangaType, type_id)
        age_rating = self._get_instance_or_none(AgeRating, age_rating_id)
        status = self._get_instance_or_none(Status, status_id)

        # Создаем Title
        title = Title.objects.create(
            type=manga_type, age_rating=age_rating, status=status, **validated_data
        )

        self._set_m2m_relations(title, Category, category_ids, "categories")
        self._set_m2m_relations(title, Genre, genre_ids, "genres")

        return title

    def update(self, instance, validated_data):
        request = self.context.get("request")

        type_id = request.data.get("type")
        age_rating_id = request.data.get("age_rating")
        status_id = request.data.get("status")
        category_ids = request.data.get("categories")
        genre_ids = request.data.get("genres")

        # Обновляем связанные поля
        if "type" in request.data:
            instance.type = self._get_instance_or_none(MangaType, type_id)

        if "age_rating" in request.data:
            instance.age_rating = self._get_instance_or_none(AgeRating, age_rating_id)

        if "status" in request.data:
            instance.status = self._get_instance_or_none(Status, status_id)

        # Обновляем обычные поля
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # Обновляем ManyToMany связи
        if category_ids is None:
            pass
        else:
            self._set_m2m_relations(instance, Category, category_ids, "categories")

        if genre_ids is None:
            pass
        else:
            self._set_m2m_relations(instance, Genre, genre_ids, "genres")

        return instance

    def _get_instance_or_none(self, model, obj_id):
        if obj_id is not None:
            try:
                return model.objects.get(id=obj_id)
            except model.DoesNotExist:
                raise serializers.ValidationError(
                    {f"{model.__name__.lower()}_id": f"Объект с ID {obj_id} не найден."}
                )
        return None

    def _set_m2m_relations(self, instance, related_model, ids, field_name):
        """
        Универсально устанавливает ManyToMany связи для указанного поля.

        :param instance: экземпляр модели Title
        :param related_model: связанная модель (например, Category, Genre)
        :param ids: список ID для связи
        :param field_name: имя ManyToMany поля в модели Title
        """
        if not ids:
            getattr(instance, field_name).clear()
            return

        # Получаем существующие объекты по ID
        queryset = related_model.objects.filter(id__in=ids)
        valid_ids = list(queryset.values_list("id", flat=True))

        # Проверка на несуществующие ID
        if len(valid_ids) != len(ids):
            invalid_ids = set(ids) - set(valid_ids)
            raise serializers.ValidationError(
                {field_name: f"Некоторые ID не найдены: {invalid_ids}"}
            )

        # Устанавливаем связи
        getattr(instance, field_name).set(queryset)
