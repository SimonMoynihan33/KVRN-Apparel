# Generated by Django 3.2.25 on 2024-10-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_main_category',
            field=models.BooleanField(default=False),
        ),
    ]
