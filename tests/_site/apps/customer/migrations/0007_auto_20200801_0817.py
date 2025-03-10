# Generated by Django 3.0.8 on 2020-08-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0006_auto_20190430_1736"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productalert",
            options={
                "ordering": ["-date_created"],
                "verbose_name": "Product alert",
                "verbose_name_plural": "Product alerts",
            },
        ),
        migrations.AlterField(
            model_name="productalert",
            name="date_created",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Date created"
            ),
        ),
    ]
