# Generated by Django 3.2 on 2021-04-28 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210416_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ak',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 18, 44, 50, 569368, tzinfo=utc)),
        ),
    ]
