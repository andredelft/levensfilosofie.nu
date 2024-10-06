# Generated by Django 3.2.15 on 2024-10-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0012_symposium_entrance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symposium',
            name='entrance',
            field=models.CharField(choices=[('voluntary', 'Vrijwillige bijdrage'), ('free', 'Vrij')], default='voluntary', max_length=10, verbose_name='Toegang'),
        ),
    ]