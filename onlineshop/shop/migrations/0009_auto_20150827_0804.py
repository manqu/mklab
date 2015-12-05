# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_item_categoriy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categoriy',
            new_name='categories',
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
