# Generated by Django 5.1.2 on 2025-01-10 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0006_osoba_data_dodania'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osoba',
            name='data_dodania',
        ),
    ]
