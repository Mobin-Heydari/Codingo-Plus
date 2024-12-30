# Generated by Django 5.1.3 on 2024-12-30 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='اسلاگ')),
                ('icon', models.ImageField(upload_to='plans/icon/', verbose_name='آیکون')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'پلن اصلی',
                'verbose_name_plural': 'پلن های اصلی',
            },
        ),
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plans.mainplans', verbose_name='پلن')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.subservice', verbose_name='سرویس')),
            ],
            options={
                'verbose_name': 'پلن سرویس',
                'verbose_name_plural': 'پلن های سرویس',
            },
        ),
        migrations.CreateModel(
            name='PlanSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_support', models.IntegerField(default=6, verbose_name='پشتیبانی رایگان')),
                ('supporting_price_per_month', models.BigIntegerField(verbose_name='هزینه ی پشتیبانی ماهانه')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supports', to='Plans.serviceplan', verbose_name='پلن')),
            ],
            options={
                'verbose_name': 'پشتیبانی',
                'verbose_name_plural': 'پشتیبانی ها',
            },
        ),
        migrations.CreateModel(
            name='PlansFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_features', to='Services.feature', verbose_name='امکانات')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='Plans.serviceplan', verbose_name='پلن')),
            ],
            options={
                'verbose_name': 'ویژگی سرویس',
                'verbose_name_plural': 'ویژگی های سرویس',
            },
        ),
        migrations.CreateModel(
            name='PlanPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_price', models.BigIntegerField(verbose_name='کف قیمت')),
                ('max_price', models.BigIntegerField(verbose_name='بالاترین قیمت')),
                ('payment_steps', models.IntegerField(verbose_name='تعداد مراحل پرداخت')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='Plans.serviceplan', verbose_name='پلن')),
            ],
            options={
                'verbose_name': 'قیمت پلن',
                'verbose_name_plural': 'قیمت های پلن',
            },
        ),
    ]
