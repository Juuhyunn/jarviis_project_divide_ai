# Generated by Django 3.2.5 on 2021-12-13 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0006_alter_userlog_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 14, 1, 46, 31, 275944)),
        ),
    ]