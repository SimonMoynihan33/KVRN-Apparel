# Generated by Django 4.2 on 2024-11-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_submissions', '0003_userdesignsubmission_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdesignsubmission',
            name='email',
            field=models.EmailField(default='not_provided@example.com', max_length=254),
            preserve_default=False,
        ),
    ]