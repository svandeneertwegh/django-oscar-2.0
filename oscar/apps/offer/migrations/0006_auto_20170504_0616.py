# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0005_auto_20170423_1217"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conditionaloffer",
            name="end_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Offers are active until the end date. Leave this empty if the offer has no expiry date.",
                null=True,
                verbose_name="End date",
            ),
        ),
        migrations.AlterField(
            model_name="conditionaloffer",
            name="start_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Offers are active from the start date. Leave this empty if the offer has no start date.",
                null=True,
                verbose_name="Start date",
            ),
        ),
    ]
