# Generated by Django 2.2.3 on 2019-07-08 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0003_auto_20190708_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biomodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='biomodel',
            name='bmKey',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='biomodel',
            name='saveDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 10, 24, 5, 39737)),
        ),
    ]