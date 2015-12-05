# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20151109_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.ImageField(null=True, upload_to=shop.utils.random_name_upload_to, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
