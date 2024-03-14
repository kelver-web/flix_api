from django.db import models

from genres.models import Genre
from actors.models import Actors

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actors, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-release_date']
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
