# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-15 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0003_auto_20161120_1707"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="conditionaloffer",
            options={
                "ordering": ["-priority", "pk"],
                "verbose_name": "Conditional offer",
                "verbose_name_plural": "Conditional offers",
            },
        ),
    ]
