# Generated by Django 3.2.3 on 2021-07-31 16:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=7)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('reviewer', models.TextField()),
                ('reviewer_address', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 7, 31, 22, 51, 32, 824806))),
            ],
        ),
        migrations.AlterField(
            model_name='yelpbusinessitem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 22, 51, 32, 823806)),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.yelpbusinessitem'),
        ),
    ]
