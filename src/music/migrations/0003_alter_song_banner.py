# Generated by Django 5.0.7 on 2024-07-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0002_alter_song_banner_alter_song_song_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="banner",
            field=models.FileField(upload_to="banner/"),
        ),
    ]
