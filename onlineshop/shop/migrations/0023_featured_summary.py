# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20150906_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='summary',
            field=models.CharField(max_length=150, default=datetime.datetime(2015, 9, 6, 11, 44, 23, 986869, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
