# Generated by Django 4.0 on 2024-01-31 20:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]