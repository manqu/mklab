# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20151116_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(related_name='item_image', to='shop.Item', null=True, blank=True),
        ),
    ]
