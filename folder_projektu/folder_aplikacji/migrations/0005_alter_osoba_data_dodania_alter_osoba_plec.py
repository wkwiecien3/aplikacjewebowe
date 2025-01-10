# Generated by Django 5.1.2 on 2025-01-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0004_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default='2025-01-10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna')], default=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna')]),
        ),
    ]
