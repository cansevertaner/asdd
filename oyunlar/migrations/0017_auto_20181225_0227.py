# Generated by Django 2.0.9 on 2018-12-24 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0016_auto_20181225_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_file',
            field=models.FileField(default='', upload_to='oyunlar/static/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 2, 27, 11, 119438)),
        ),
    ]
