# Generated by Django 2.2.3 on 2019-07-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biomodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmKey', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
