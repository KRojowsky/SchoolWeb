# Generated by Django 3.2.19 on 2023-09-03 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_newteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='newteacher',
            name='age',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='newteacher',
            name='language',
            field=models.CharField(choices=[('tak', 'Tak'), ('nie', 'Nie')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='newteacher',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Numer telefonu musi byc w formacie: '999 999 999'. Maksymalnie 15 cyfr.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='newteacher',
            name='school',
            field=models.CharField(choices=[('podstawowa', 'Szkoła podstawowa'), ('średnia', 'Szkoła średnia'), ('maturalna', 'Klasa maturalna'), ('praktyki', 'Praktyki'), ('licencjat', 'Licencjat'), ('magister', 'Magister'), ('inżynier', 'Inżynier'), ('doktor', 'Doktor')], max_length=20, null=True),
        ),
    ]
