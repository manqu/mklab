# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150906_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='image',
        ),
        migrations.AddField(
            model_name='featuredmainimage',
            name='featured',
            field=models.ForeignKey(blank=True, null=True, related_name='image', to='shop.Featured'),
        ),
    ]
