# Generated by Django 5.1.2 on 2024-11-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_remove_product_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='a',
            field=models.TextField(blank=True, null=True),
        ),
    ]
