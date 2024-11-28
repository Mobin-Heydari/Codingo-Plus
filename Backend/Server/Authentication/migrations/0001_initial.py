# Generated by Django 5.1.3 on 2024-11-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('EXP', 'Expired'), ('ACT', 'Active')], default='ACT', max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=40)),
                ('user_type', models.CharField(max_length=3)),
                ('password', models.CharField(max_length=16)),
                ('token', models.CharField(max_length=250, unique=True)),
                ('code', models.CharField(max_length=6)),
                ('expiration', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'One-Time Password',
                'verbose_name_plural': 'One-Time Passwords',
            },
        ),
    ]