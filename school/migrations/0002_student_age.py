# Generated by Django 4.1.3 on 2022-11-30 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=datetime.datetime(2022, 11, 30, 8, 47, 2, 735209, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
