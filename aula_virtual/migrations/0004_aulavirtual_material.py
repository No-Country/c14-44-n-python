# Generated by Django 4.2.6 on 2023-10-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_virtual', '0003_alter_aulavirtual_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='aulavirtual',
            name='material',
            field=models.FileField(default=2, upload_to='', verbose_name='material'),
            preserve_default=False,
        ),
    ]