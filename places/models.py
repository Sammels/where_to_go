from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    title_short = models.CharField(max_length=40, default="")
    placeID = models.SlugField(max_length=100, verbose_name='ID места', default='')
    description_short = models.TextField(blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField(upload_to='place_images', verbose_name='Изображение')
    image_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering=['image_order']

    def __str__(self):
        return f"{self.pk} {self.place.title}"


