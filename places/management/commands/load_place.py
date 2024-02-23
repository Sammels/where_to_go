import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'place_url',
            type=str,
            help='Ссылка на информацию о локации',
        )

    def handle(self, *args, **options):
        url = options['place_url']
        response = requests.get(url)
        response.raise_for_status()
        place_raw = response.json()
        place, _ = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults={
                'short_description': place_raw['description_short'],
                'long_description': place_raw['description_long'],
                'lat': place_raw['coordinates']['lat'],
                'lon': place_raw['coordinates']['lng'],
            },
        )

        image_urls = place_raw['imgs']
        for image_url in image_urls:
            response = requests.get(image_url)
            response.raise_for_status()
            image_content = ContentFile(response.content, name=os.path.split(image_url)[1])
            Image.objects.create(place=place, image=image_content)
