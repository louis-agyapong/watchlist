# Generated by Django 4.1.3 on 2022-11-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist", "0001_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="Description"),
        ),
    ]