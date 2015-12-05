# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20151116_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(to='shop.Category', default=1),
            preserve_default=False,
        ),
    ]
