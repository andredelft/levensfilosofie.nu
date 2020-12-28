# Generated by Django 3.0.8 on 2020-12-28 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0002_add_indexes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programitem',
            name='time',
        ),
        migrations.RemoveField(
            model_name='symposium',
            name='time',
        ),
        migrations.AddField(
            model_name='programitem',
            name='time_from',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programitem',
            name='time_to',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='symposium',
            name='time_from',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='symposium',
            name='time_to',
            field=models.TimeField(null=True),
        ),
    ]
