# Generated by Django 5.2.1 on 2025-06-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('init', '0005_image_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='observacao',
            field=models.CharField(default='Sem observação', max_length=1000),
        ),
    ]
