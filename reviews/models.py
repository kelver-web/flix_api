from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie

# Create your models here.


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas.'),
        ]
    )
    comments = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-stars']
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.movie}'
