# Generated by Django 2.0.9 on 2018-12-24 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0015_auto_20181225_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 2, 0, 26, 624779)),
        ),
        migrations.AlterField(
            model_name='games',
            name='game_img',
            field=models.FileField(upload_to='oyunlar/static/images'),
        ),
    ]
