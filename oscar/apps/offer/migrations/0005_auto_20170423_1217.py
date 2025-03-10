# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0004_auto_20170415_1518"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conditionaloffer",
            name="benefit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="offers",
                to="offer.Benefit",
                verbose_name="Benefit",
            ),
        ),
        migrations.AlterField(
            model_name="conditionaloffer",
            name="condition",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="offers",
                to="offer.Condition",
                verbose_name="Condition",
            ),
        ),
    ]
