# Generated by Django 4.0.3 on 2022-03-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_animation_main_music_main_photo_main_simulation_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='animation',
            name='image',
            field=models.BooleanField(default=False),
        ),
    ]
