# Generated by Django 2.2.3 on 2019-07-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biomodel',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
    ]
