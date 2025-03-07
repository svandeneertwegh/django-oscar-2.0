# Generated by Django 5.1.1 on 2024-11-05 14:16
from django.db import migrations
from django.db.models import Q
from django.contrib.auth import get_user_model


def assign_permissions_to_staff_users(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    dashboard_permissions_group, _ = Group.objects.get_or_create(
        name="All Oscar Dashboard Permissions"
    )
    User = get_user_model()
    UserGroup = User.groups.through
    user_groups = []

    permission_codes = [
        # Catalogue
        "catalogue.add_product",
        "catalogue.change_product",
        "catalogue.view_product",
        "catalogue.delete_product",
        "catalogue.add_category",
        "catalogue.change_category",
        "catalogue.view_category",
        "catalogue.delete_category",
        "catalogue.add_productclass",
        "catalogue.change_productclass",
        "catalogue.view_productclass",
        "catalogue.delete_productclass",
        "catalogue.add_attributeoptiongroup",
        "catalogue.change_attributeoptiongroup",
        "catalogue.view_attributeoptiongroup",
        "catalogue.delete_attributeoptiongroup",
        "catalogue.add_option",
        "catalogue.change_option",
        "catalogue.view_option",
        "catalogue.delete_option",
        # Communications
        "communication.add_communicationeventtype",
        "communication.change_communicationeventtype",
        "communication.view_communicationeventtype",
        "communication.delete_communicationeventtype",
        # Partners
        "partner.add_stockalert",
        "partner.change_stockalert",
        "partner.view_stockalert",
        "partner.delete_stockalert",
        "partner.add_partner",
        "partner.change_partner",
        "partner.view_partner",
        "partner.delete_partner",
        # Offers
        "offer.add_conditionaloffer",
        "offer.change_conditionaloffer",
        "offer.view_conditionaloffer",
        "offer.delete_conditionaloffer",
        # Orders
        "order.add_order",
        "order.change_order",
        "order.view_order",
        "order.delete_order",
        # Flat Pages
        "flatpages.add_flatpage",
        "flatpages.change_flatpage",
        "flatpages.view_flatpage",
        "flatpages.delete_flatpage",
        # Ranges
        "offer.add_range",
        "offer.change_range",
        "offer.view_range",
        "offer.delete_range",
        # Analytics
        "analytics.add_userrecord",
        "analytics.change_userrecord",
        "analytics.view_userrecord",
        "analytics.delete_userrecord",
        # Reviews
        "reviews.add_productreview",
        "reviews.change_productreview",
        "reviews.view_productreview",
        "reviews.delete_productreview",
        # Shipping
        "add_weightbased",
        "change_weightbased",
        "delete_weightbased",
        "view_weightbased",
        # Users
        f"{User._meta.app_label}.add_user",
        f"{User._meta.app_label}.change_user",
        f"{User._meta.app_label}.view_user",
        f"{User._meta.app_label}.delete_user",
        # Vouchers
        "voucher.add_voucher",
        "voucher.change_voucher",
        "voucher.view_voucher",
        "voucher.delete_voucher",
    ]

    filters = Q()
    for code in permission_codes:
        app_label, __, codename = code.partition(".")
        filters |= Q(content_type__app_label=app_label, codename=codename)
    permissions = Permission.objects.filter(filters)
    dashboard_permissions_group.permissions.set(permissions)
    dashboard_permissions_group.save()

    for user_id in User.objects.filter(is_staff=True, is_superuser=False).values_list(
        "id", flat=True
    ):
        user_groups.append(
            UserGroup(user_id=user_id, group_id=dashboard_permissions_group.id)
        )
    UserGroup.objects.bulk_create(user_groups)


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0001_initial"),
        ("catalogue", "0001_initial"),
        ("communication", "0001_initial"),
        ("customer", "0007_auto_20200801_0817"),
        ("flatpages", "0001_initial"),
        ("offer", "0001_initial"),
        ("offer", "0001_initial"),
        ("order", "0001_initial"),
        ("partner", "0001_initial"),
        ("reviews", "0001_initial"),
        ("voucher", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            assign_permissions_to_staff_users, migrations.RunPython.noop
        )
    ]
