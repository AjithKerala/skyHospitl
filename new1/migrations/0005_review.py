# Generated by Django 4.1.7 on 2023-05-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new1', '0004_booking22'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
