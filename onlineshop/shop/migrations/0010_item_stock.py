# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20150827_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
