# Generated by Django 2.0.7 on 2018-07-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analise', '0014_auto_20180716_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidaeletromagnetica',
            name='dado',
            field=models.FilePathField(default='/', path='/home/mathias/Área de Trabalho/mtd_git/MTD/eletromagnetico/interfaceAnalise', recursive=True),
        ),
        migrations.AlterField(
            model_name='medidor',
            name='foto',
            field=models.FilePathField(default='/', path='/home/mathias/Área de Trabalho/mtd_git/MTD/eletromagnetico/interfaceAnalise', recursive=True),
        ),
    ]
