# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_featuredmainimage_main_iamge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredmainimage',
            name='main_iamge',
        ),
        migrations.AddField(
            model_name='featured',
            name='main_image',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='featuredmainimage',
            name='image',
            field=models.ImageField(null=True, upload_to=shop.utils.random_name_upload_to, blank=True),
        ),
    ]
