from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"  # используем email для входа
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangaType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AgeRating(models.Model):
    AGE_RATING_CHOICES = [
        ("Для всех", "Для всех"),
        ("16+", "16+"),
        ("18+", "18+"),
    ]

    name = models.CharField(max_length=10, choices=AGE_RATING_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    STATUS_CHOICES = [
        ("Продолжается", "Продолжается"),
        ("Закончен", "Закончен"),
        ("Заморожен", "Заморожен"),
        ("Нет переводчика", "Нет переводчика"),
    ]

    name = models.CharField(max_length=50, choices=STATUS_CHOICES, unique=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name
