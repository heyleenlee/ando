# Generated by Django 3.2.8 on 2022-06-30 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.IntegerField(default=0)),
                ('UserId', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=20)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Remark', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2022, 6, 30, 17, 36, 23, 825250))),
                ('updatedAt', models.DateTimeField(default=datetime.datetime(2022, 6, 30, 17, 36, 23, 825250))),
            ],
            options={
                'db_table': 'AssetCash',
            },
        ),
    ]
