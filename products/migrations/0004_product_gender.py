# Generated by Django 5.1.2 on 2024-10-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('men', 'Men'), ('women', 'Women')], max_length=10, null=True),
        ),
    ]
