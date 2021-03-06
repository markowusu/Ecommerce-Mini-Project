# Generated by Django 3.2.3 on 2021-07-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255),
        ),
    ]
