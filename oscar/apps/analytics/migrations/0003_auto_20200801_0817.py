# Generated by Django 3.0.8 on 2020-08-01 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_auto_20140827_1705"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userproductview",
            options={
                "ordering": ["-pk"],
                "verbose_name": "User product view",
                "verbose_name_plural": "User product views",
            },
        ),
        migrations.AlterModelOptions(
            name="usersearch",
            options={
                "ordering": ["-pk"],
                "verbose_name": "User search query",
                "verbose_name_plural": "User search queries",
            },
        ),
    ]
