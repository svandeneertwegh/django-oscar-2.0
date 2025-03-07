# Generated by Django 2.1.7 on 2019-03-01 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0007_auto_20181115_1953"),
        ("communication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communicationevent",
            name="event_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="communication.CommunicationEventType",
                verbose_name="Event Type",
            ),
        ),
    ]
