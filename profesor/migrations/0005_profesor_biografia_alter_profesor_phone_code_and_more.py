# Generated by Django 4.1.5 on 2023-10-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0004_alter_profesor_phone_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='phone_code',
            field=models.IntegerField(verbose_name='Código de Teléfono'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='phone_number',
            field=models.IntegerField(verbose_name='Número de Teléfono'),
        ),
    ]
