# Generated by Django 4.2.11 on 2024-06-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelService', '0002_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
