# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '0014_auto_20150902_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(default='1', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
