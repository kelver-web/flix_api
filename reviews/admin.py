from django.contrib import admin

from reviews.models import Review


# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'stars', 'comments', 'movie')
    list_filter = ('stars',)
