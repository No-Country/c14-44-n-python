# Generated by Django 4.2.6 on 2023-11-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_virtual', '0004_aulavirtual_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aulavirtual',
            name='material',
            field=models.CharField(max_length=10000, verbose_name='material'),
        ),
    ]
