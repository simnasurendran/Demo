# Generated by Django 5.0.1 on 2024-01-30 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_remove_movie_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
