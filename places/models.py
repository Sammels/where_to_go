from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    title_short = models.CharField(max_length=40, default="")
    placeID = models.SlugField(max_length=100, verbose_name='ID места', default='')
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField(upload_to='place_images', verbose_name='Изображение')

    def __str__(self):
        return f"{self.pk} {self.place.title}"
