# Generated by Django 4.1.3 on 2022-11-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="streamingplatform",
            name="is_deleted",
        ),
        migrations.AlterField(
            model_name="movie",
            name="is_deleted",
            field=models.BooleanField(default=True, verbose_name="Is Deleted"),
        ),
    ]