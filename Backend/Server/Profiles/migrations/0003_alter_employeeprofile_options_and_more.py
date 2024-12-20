# Generated by Django 5.1.3 on 2024-12-04 12:47

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_remove_employeeprofile_skils_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeprofile',
            options={'verbose_name': 'پروفایل کارمند', 'verbose_name_plural': 'پروفایل\u200cهای کارمندان'},
        ),
        migrations.AlterModelOptions(
            name='employeeskills',
            options={'verbose_name': 'مهارت کارمند', 'verbose_name_plural': 'مهارت\u200cهای کارمندان'},
        ),
        migrations.AlterModelOptions(
            name='simpleuserprofile',
            options={'verbose_name': 'پروفایل کاربر ساده', 'verbose_name_plural': 'پروفایل\u200cهای کاربران ساده'},
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='بیوگرافی'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Employee_Profile', to=settings.AUTH_USER_MODEL, verbose_name='کارمند'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='employee_stack',
            field=models.CharField(blank=True, choices=[('DES', 'طراح'), ('DEV', 'توسعه\u200cدهنده'), ('MAN', 'مدیر')], default='DEV', max_length=3, null=True, verbose_name='نوع شغل'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان شغلی'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/employees-profiles/', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=1, verbose_name='سال\u200cهای تجربه'),
        ),
        migrations.AlterField(
            model_name='employeeskills',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_skills', to='Profiles.employeeprofile', verbose_name='کارمند'),
        ),
        migrations.AlterField(
            model_name='employeeskills',
            name='mastery',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='سطح تسلط'),
        ),
        migrations.AlterField(
            model_name='employeeskills',
            name='skill',
            field=models.CharField(max_length=255, verbose_name='مهارت'),
        ),
        migrations.AlterField(
            model_name='simpleuserprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='بیوگرافی'),
        ),
        migrations.AlterField(
            model_name='simpleuserprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='simpleuserprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/simple-user-profiles/', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='simpleuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User_Profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
