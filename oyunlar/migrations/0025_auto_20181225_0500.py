# Generated by Django 2.0.9 on 2018-12-25 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0024_auto_20181225_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='game_img2',
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 5, 0, 11, 131296)),
        ),
    ]