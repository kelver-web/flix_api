from django.contrib import admin

from . models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'genre', 'resume')
    list_filter = ('title', 'release_date', 'genre',)
