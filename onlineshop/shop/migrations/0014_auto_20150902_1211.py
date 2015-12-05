# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.utils
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '0013_auto_20150827_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='main_image',
            field=models.ImageField(upload_to=shop.utils.random_name_upload_to, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='object_id',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
