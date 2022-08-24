# Generated by Django 3.2.3 on 2022-06-30 03:43

from django.db import migrations


from api_product.constant.Data import ProductData


def initial_product_data(apps, schema_editor):
    product_model = apps.get_model("api_product", "Product")

    products = []

    for product in ProductData.products:
        products.append(product_model(
            id=product['id'],
            name=product['name'],
            description=product['description'],
            price=product['price'],
            color=product['color'],
            slug=product['slug'],
            image=product["image"],
            category_id=product['category_id'],
        ))

    product_model.objects.bulk_create(products)


class Migration(migrations.Migration):
    dependencies = [
        ('api_product', '0002_migrate_categories'),
    ]

    operations = [
        migrations.RunPython(initial_product_data, migrations.RunPython.noop)
    ]