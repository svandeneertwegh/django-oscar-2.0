# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_auto_20160802_1358"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreview",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="catalogue.Product",
            ),
        ),
    ]
