# Generated by Django 2.2.6 on 2019-10-02 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20191002_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 2, 18, 6, 44, 959383)),
        ),
    ]