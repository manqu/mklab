# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20150906_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredmainimage',
            name='featured',
        ),
        migrations.AddField(
            model_name='featured',
            name='image',
            field=models.ForeignKey(null=True, blank=True, to='shop.FeaturedMainImage'),
        ),
    ]
