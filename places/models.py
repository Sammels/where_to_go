from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    coordinates = models.JSONField(blank=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.id} {self.title}"
