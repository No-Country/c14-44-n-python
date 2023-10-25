# Generated by Django 4.2.6 on 2023-10-25 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_alter_alumno_code_alter_alumno_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='code',
        ),
        migrations.AddField(
            model_name='alumno',
            name='phone_code',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(10)], verbose_name='Número de Teléfono'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='phone_number',
            field=models.IntegerField(default=1000000000, validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(1000000000)], verbose_name='Número de Teléfono'),
        ),
    ]
