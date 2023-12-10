from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    class GalareyInline(admin.TabularInline):
        model = models.Galarey
        max_num = 1

    list_display = ('id', 'Title', 'Year')
    inlines = (GalareyInline,)

