# Generated by Django 3.2.7 on 2021-11-07 22:54

from django.db import migrations
import levensfilosofie.fields


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0003_zoom_title_TBA'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=levensfilosofie.fields.CleanHTMLField(blank=True, null=True, verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='personalia',
            field=levensfilosofie.fields.CleanHTMLField(blank=True, null=True, verbose_name='Personalia'),
        ),
    ]
