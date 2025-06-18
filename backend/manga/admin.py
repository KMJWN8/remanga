from django.contrib import admin

from .models import AgeRating, Category, Genre, MangaType, Title

admin.site.register(AgeRating)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(MangaType)
admin.site.register(Title)
