# Generated by Django 2.0.9 on 2018-12-25 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0028_auto_20181225_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='img_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 5, 37, 58, 246161)),
        ),
    ]
