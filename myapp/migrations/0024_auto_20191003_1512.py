# Generated by Django 2.2.6 on 2019-10-03 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20191003_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 15, 12, 44, 2365)),
        ),
    ]