# Generated by Django 3.2.3 on 2021-09-20 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210731_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 23, 57, 7, 703306)),
        ),
        migrations.AlterField(
            model_name='yelpbusinessitem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 23, 57, 7, 703306)),
        ),
    ]
