# Generated by Django 3.2.3 on 2021-07-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_content',
            field=models.TextField(blank=True),
        ),
    ]
