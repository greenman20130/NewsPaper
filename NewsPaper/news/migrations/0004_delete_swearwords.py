# Generated by Django 5.0 on 2024-01-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_subscribers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SwearWords',
        ),
    ]
