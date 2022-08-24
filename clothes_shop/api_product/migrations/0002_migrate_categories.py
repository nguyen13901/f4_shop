from django.db import migrations, models

from api_product.constant.Data import CategoryData


def initial_category_data(apps, schema_editor):
    category_model = apps.get_model("api_product", "Category")
    categories = []

    for category in CategoryData.categories:
        categories.append(category_model(id=category["id"], name=category["name"], slug=category["slug"]))

    category_model.objects.bulk_create(categories)


def delete_all_data(apps, schema_editor):
    category_model = apps.get_model("api_product", "Category")

    category_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api_product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_category_data, delete_all_data)
    ]