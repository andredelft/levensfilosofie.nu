# Generated by Django 3.1.5 on 2021-09-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0009_clean_HTML'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='video_id',
            field=models.CharField(blank=True, help_text='De ID is het deel van de YouTube URL direct na "v=", altijd 11 karakters lang. Bijvoorbeeld: https://www.youtube.com/watch?v=<b>dQw4w9WgXcQ</b>', max_length=20, null=True, verbose_name='YouTube video ID'),
        ),
    ]
