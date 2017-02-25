from __future__ import unicode_literals

from decimal import Decimal
from django.db import models


class Movie(models.Model):
    title = models.CharField(
        verbose_name='Movie Title',
        max_length=255
    )
    genre = models.CharField(
        verbose_name='Genre',
        max_length=255
    )
    rating = models.DecimalField(
        verbose_name='Rating out of 10',
        default=Decimal(0),
        max_digits=5,
        decimal_places=2
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=1000
    )
    casting = models.CharField(
        verbose_name='Castings for the Movie',
        max_length=1000
    )

    class Meta:
        db_table = 'movie'
        app_label = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
