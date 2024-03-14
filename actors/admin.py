from django.contrib import admin

from actors.models import Actors

# Register your models here.


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality',)
    list_filter = ('name', 'birthday',)
