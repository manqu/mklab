# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20151114_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to=shop.utils.random_name_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(to='shop.Item', blank=True, null=True),
        ),
    ]
