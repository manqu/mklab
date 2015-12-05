# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20150906_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredmainimage',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 9, 6, 10, 54, 30, 620829, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
