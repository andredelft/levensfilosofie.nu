# Generated by Django 3.1.5 on 2021-09-27 13:15

from django.db import migrations, models
import django.db.models.deletion
import levensfilosofie.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('content', levensfilosofie.fields.CleanHTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.TimeField(verbose_name='Begintijd')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Eindtijd')),
                ('name', levensfilosofie.fields.CleanHTMLLineField(verbose_name='Naam')),
            ],
            options={
                'verbose_name': 'Programma-item',
                'verbose_name_plural': 'Programma-items',
            },
        ),
        migrations.CreateModel(
            name='Symposium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', levensfilosofie.fields.CleanHTMLLineField(verbose_name='Titel')),
                ('introduction', levensfilosofie.fields.CleanHTMLField(blank=True, null=True, verbose_name='Introductie')),
                ('date', models.DateField(unique=True, verbose_name='Datum')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='Begintijd')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='Eindtijd')),
                ('place', models.CharField(blank=True, max_length=200, null=True, verbose_name='Locatie')),
                ('zoom_instructions', models.BooleanField(default=False, verbose_name='Zoom instructies')),
                ('meeting_ID', models.CharField(blank=True, max_length=15, null=True, verbose_name='Meeting ID')),
                ('password', models.CharField(blank=True, max_length=15, null=True, verbose_name='Wachtwoord')),
                ('include_vids', models.JSONField(default=list)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Symposium',
                'verbose_name_plural': 'Symposia',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', levensfilosofie.fields.CleanHTMLLineField(verbose_name='Titel')),
                ('speaker', models.CharField(max_length=200, verbose_name='Spreker')),
                ('abstract', levensfilosofie.fields.CleanHTMLField(verbose_name='Abstract')),
                ('personalia', levensfilosofie.fields.CleanHTMLField(verbose_name='Personalia')),
                ('video_id', models.CharField(blank=True, help_text='De ID is het deel van de YouTube URL direct na "v=", altijd 11 karakters lang. Bijvoorbeeld: https://www.youtube.com/watch?v=<b>dQw4w9WgXcQ</b>', max_length=20, null=True, verbose_name='YouTube video ID')),
                ('symposium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annonces.symposium')),
            ],
            options={
                'verbose_name': 'Lezing',
                'verbose_name_plural': 'Lezingen',
            },
        ),
        migrations.AddIndex(
            model_name='symposium',
            index=models.Index(fields=['slug'], name='annonces_sy_slug_130bb0_idx'),
        ),
        migrations.AddIndex(
            model_name='symposium',
            index=models.Index(fields=['-date'], name='annonces_sy_date_f17a6c_idx'),
        ),
        migrations.AddField(
            model_name='programitem',
            name='symposium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annonces.symposium'),
        ),
    ]
