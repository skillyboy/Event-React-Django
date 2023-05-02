# Generated by Django 4.2 on 2023-05-01 01:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("location", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="event_images/")),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="liked_events", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
