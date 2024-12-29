# Generated by Django 5.1.3 on 2024-12-29 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام سرویس')),
                ('slug', models.SlugField(max_length=255, verbose_name='اسلاگ')),
                ('imgae', models.ImageField(upload_to='services/images', verbose_name='تصویر ')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'سرویس اصلی',
                'verbose_name_plural': 'سرویس های اصلی',
            },
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('slug', models.SlugField(max_length=255, verbose_name='اسلاگ')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('sub_content', models.CharField(max_length=100, verbose_name='محتوای مخصر')),
                ('image', models.ImageField(upload_to='services/images', verbose_name='تصویر')),
                ('icon', models.ImageField(upload_to='Sub-services/icons', verbose_name='آیکوهن')),
            ],
        ),
        migrations.CreateModel(
            name='SubServiceFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('icon', models.ImageField(upload_to='Sub-services/Features/icons', verbose_name='آیکون')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.subservice', verbose_name='خدمت')),
            ],
        ),
    ]