# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partner", "0004_auto_20160107_1755"),
    ]

    operations = [
        migrations.AddField(
            model_name="stockrecord",
            name="offer_name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
