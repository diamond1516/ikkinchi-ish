from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Player)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.Club)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.Footer)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

    def has_add_permission(self, request): return not models.Footer.objects.exists()
