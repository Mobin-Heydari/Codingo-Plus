# Generated by Django 5.1.3 on 2024-12-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0005_category_project_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=100, unique=True, verbose_name='دسته بندی'),
        ),
    ]
