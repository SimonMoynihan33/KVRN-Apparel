# Generated by Django 4.2 on 2024-11-04 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design_submissions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdesignsubmission',
            name='category',
        ),
    ]
