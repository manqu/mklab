# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_featured_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='category',
            name='items',
        ),
        migrations.AddField(
            model_name='category',
            name='items',
            field=models.ForeignKey(blank=True, to='shop.Item', default=1),
            preserve_default=False,
        ),
    ]
