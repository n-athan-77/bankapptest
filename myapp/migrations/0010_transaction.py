# Generated by Django 2.2.6 on 2019-10-02 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_merge_20191002_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_debited', models.BooleanField(default=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2019, 10, 2, 17, 28, 3, 617068))),
                ('acc_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Account')),
            ],
        ),
    ]