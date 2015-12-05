# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_featured_featuredmainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredmainimage',
            name='featured',
            field=models.ForeignKey(related_name='images', to='shop.Featured'),
        ),
    ]
