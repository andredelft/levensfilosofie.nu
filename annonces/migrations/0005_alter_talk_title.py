# Generated by Django 3.2.7 on 2021-11-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0004_only_require_talk_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Titel'),
        ),
    ]
