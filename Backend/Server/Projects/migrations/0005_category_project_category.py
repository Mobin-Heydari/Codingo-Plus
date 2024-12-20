# Generated by Django 5.1.3 on 2024-12-11 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_alter_project_options_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/images/', verbose_name='تصویر')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.category', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
