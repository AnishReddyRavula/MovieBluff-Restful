# Generated by Django 2.0.2 on 2018-02-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movies_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='watched_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
