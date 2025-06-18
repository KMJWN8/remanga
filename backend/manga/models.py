from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)


class MangaType(models.Model):
    name = models.CharField(max_length=100)


class AgeRating(models.Model):
    AGE_RATING_CHOICES = [
        ("Для всех", "Для всех"),
        ("16+", "16+"),
        ("18+", "18+"),
    ]

    name = models.CharField(max_length=10, choices=AGE_RATING_CHOICES, unique=True)


class Status(models.Model):
    STATUS_CHOICES = [
        ("prodolzhaetsja", "Продолжается"),
        ("zakonchen", "Закончен"),
        ("zamorozhen", "Заморожен"),
        ("neperevoditsjalitsenzirovano", "Не переводится (лицензировано)"),
        ("netperevodchika", "Нет переводчика"),
    ]

    name = models.CharField(max_length=50, choices=STATUS_CHOICES, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="covers/")
    type = models.ForeignKey(MangaType, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    genres = models.ManyToManyField(Genre)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.SET_NULL, null=True)
    year_released = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
