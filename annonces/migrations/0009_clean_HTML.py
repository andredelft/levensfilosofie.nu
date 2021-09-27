# Generated by Django 3.1.5 on 2021-09-26 10:25

import levensfilosofie.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0008_symposium_model_tweaks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programitem',
            options={'verbose_name': 'Programma-item', 'verbose_name_plural': 'Programma-items'},
        ),
        migrations.AlterModelOptions(
            name='symposium',
            options={'ordering': ['-date'], 'verbose_name': 'Symposium', 'verbose_name_plural': 'Symposia'},
        ),
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': 'Lezing', 'verbose_name_plural': 'Lezingen'},
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='content',
            field=levensfilosofie.fields.CleanHTMLField(),
        ),
        migrations.AlterField(
            model_name='programitem',
            name='name',
            field=levensfilosofie.fields.CleanHTMLLineField(verbose_name='Naam'),
        ),
        migrations.AlterField(
            model_name='programitem',
            name='time_from',
            field=models.TimeField(verbose_name='Begintijd'),
        ),
        migrations.AlterField(
            model_name='programitem',
            name='time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='Eindtijd'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='date',
            field=models.DateField(unique=True, verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='introduction',
            field=levensfilosofie.fields.CleanHTMLField(blank=True, null=True, verbose_name='Introductie'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='meeting_ID',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Meeting ID'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Wachtwoord'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Locatie'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='time_from',
            field=models.TimeField(blank=True, null=True, verbose_name='Begintijd'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='Eindtijd'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='title',
            field=levensfilosofie.fields.CleanHTMLLineField(verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='zoom_instructions',
            field=models.BooleanField(default=False, verbose_name='Zoom instructies'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=levensfilosofie.fields.CleanHTMLField(verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='personalia',
            field=levensfilosofie.fields.CleanHTMLField(verbose_name='Personalia'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speaker',
            field=models.CharField(max_length=200, verbose_name='Spreker'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=levensfilosofie.fields.CleanHTMLLineField(verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='video_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Video ID'),
        ),
    ]
