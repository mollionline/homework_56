# Generated by Django 4.0 on 2022-01-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_category_category_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.TextField(default='Разное', max_length=100, unique=True),
        ),
    ]
