# Generated by Django 2.0.9 on 2018-12-25 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0021_auto_20181225_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 4, 53, 53, 802594)),
        ),
    ]
