# Generated by Django 3.2.15 on 2022-09-22 13:18

from django.db import migrations, models
import levensfilosofie.fields


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0008_merge_0007_alter_symposium_zoom_link_0007_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symposium',
            name='cover_image_name',
        ),
        migrations.AddField(
            model_name='symposium',
            name='photo',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='symposium',
            name='photo_id',
            field=models.CharField(blank=True, help_text='Zie de API documentatie: https://unsplash.com/documentation', max_length=200, null=True, verbose_name='Omslagfoto (Unsplash ID)'),
        ),
        migrations.AlterField(
            model_name='symposium',
            name='canceled_message',
            field=levensfilosofie.fields.CleanHTMLField(blank=True, help_text='Zal verschijnen op de pagina van de annonce en op de startpagina, wanneer daar normaliter ook een aankondiging zou verschijnen.', verbose_name='Bericht bij het afgelasten'),
        ),
    ]
