# Generated by Django 2.2.6 on 2019-10-02 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 2, 17, 36, 3, 508999)),
        ),
    ]
