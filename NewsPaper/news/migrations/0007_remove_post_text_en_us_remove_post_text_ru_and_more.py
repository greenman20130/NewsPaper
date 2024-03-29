# Generated by Django 5.0 on 2024-02-15 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_post_type_en_us_remove_post_type_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ru',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(help_text='category name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_en_us',
            field=models.CharField(help_text='category name', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_ru',
            field=models.CharField(help_text='category name', max_length=100, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en_us', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='news.category', verbose_name='This is the help text')),
            ],
        ),
    ]
