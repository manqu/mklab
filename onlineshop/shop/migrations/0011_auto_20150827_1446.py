# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_item_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=shop.utils.random_name_upload_to, blank=True),
        ),
    ]
