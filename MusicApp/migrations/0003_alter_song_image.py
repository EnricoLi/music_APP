# Generated by Django 3.2.8 on 2022-03-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApp', '0002_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]