import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid

from api_account.constant.Data import RoleData


def initial_role_data(apps, schema_editor):
    role_model = apps.get_model("api_account", "Role")
    roles = []

    for role in RoleData:
        roles.append(role_model(id=role.value["id"], name=role.value["name"]))

    role_model.objects.bulk_create(roles)


def delete_all_data(apps, schema_editor):
    role_model = apps.get_model("api_account", "Role")

    role_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api_account', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_role_data, delete_all_data)
    ]