# Generated by Django 2.2.5 on 2019-10-02 11:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('dob', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Birth')),
                ('acc_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Branch')),
            ],
        ),
    ]