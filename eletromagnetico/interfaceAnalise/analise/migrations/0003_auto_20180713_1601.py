# Generated by Django 2.0.7 on 2018-07-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analise', '0002_auto_20180713_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidaeletromagnetica',
            name='comentarios',
            field=models.TextField(max_length=500),
        ),
    ]