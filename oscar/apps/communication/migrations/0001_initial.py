# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.autoslugfield
from django.utils.module_loading import import_string
from django.conf import settings

models_AutoField = import_string(settings.DEFAULT_AUTO_FIELD)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogue", "0013_auto_20170821_1548"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0005_auto_20181115_1953"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="CommunicationEventType",
            fields=[
                (
                    "id",
                    models_AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    oscar.models.fields.autoslugfield.AutoSlugField(
                        blank=True,
                        editable=False,
                        help_text="Code used for looking up this event programmatically",
                        max_length=128,
                        populate_from="name",
                        separator="_",
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit.",
                                regex="^[a-zA-Z_][0-9a-zA-Z_]*$",
                            )
                        ],
                        verbose_name="Code",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Order related", "Order related"),
                            ("User related", "User related"),
                        ],
                        default="Order related",
                        max_length=255,
                        verbose_name="Category",
                    ),
                ),
                (
                    "email_subject_template",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Email Subject Template",
                    ),
                ),
                (
                    "email_body_template",
                    models.TextField(
                        blank=True, null=True, verbose_name="Email Body Template"
                    ),
                ),
                (
                    "email_body_html_template",
                    models.TextField(
                        blank=True,
                        help_text="HTML template",
                        null=True,
                        verbose_name="Email Body HTML Template",
                    ),
                ),
                (
                    "sms_template",
                    models.CharField(
                        blank=True,
                        help_text="SMS template",
                        max_length=170,
                        null=True,
                        verbose_name="SMS Template",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Created"
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(auto_now=True, verbose_name="Date Updated"),
                ),
            ],
            options={
                "verbose_name": "Communication event type",
                "verbose_name_plural": "Communication event types",
                "db_table": "customer_communicationeventtype",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models_AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Email Address",
                    ),
                ),
                ("subject", models.TextField(max_length=255, verbose_name="Subject")),
                ("body_text", models.TextField(verbose_name="Body Text")),
                ("body_html", models.TextField(blank=True, verbose_name="Body HTML")),
                (
                    "date_sent",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date Sent"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emails",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Email",
                "verbose_name_plural": "Emails",
                "db_table": "customer_email",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models_AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("category", models.CharField(blank=True, max_length=255)),
                (
                    "location",
                    models.CharField(
                        choices=[("Inbox", "Inbox"), ("Archive", "Archive")],
                        default="Inbox",
                        max_length=32,
                    ),
                ),
                ("date_sent", models.DateTimeField(auto_now_add=True)),
                ("date_read", models.DateTimeField(blank=True, null=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Notification",
                "verbose_name_plural": "Notifications",
                "db_table": "customer_notification",
                "ordering": ("-date_sent",),
                "abstract": False,
            },
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
    ]
