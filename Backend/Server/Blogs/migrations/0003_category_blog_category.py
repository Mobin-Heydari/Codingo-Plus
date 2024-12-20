# Generated by Django 5.1.3 on 2024-12-13 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_alter_blog_options_alter_blogsection_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True, verbose_name='دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/images/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='Blogs.category', verbose_name='دسته بندی'),
            preserve_default=False,
        ),
    ]
