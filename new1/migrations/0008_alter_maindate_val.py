# Generated by Django 4.1.7 on 2023-05-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0007_maindate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindate',
            name='val',
            field=models.DateField(),
        ),
    ]
