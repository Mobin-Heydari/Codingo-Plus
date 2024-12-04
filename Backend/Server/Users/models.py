from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from . import managers


from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.db import models

from . import managers


class User(AbstractBaseUser , PermissionsMixin):
    
    class UserTypes(models.TextChoices):
        SIMPLE_USER = "SMP", "کاربر ساده"
        EMPLOYEE = "EMP", "کارمند"
        ADMIN = "ADM", "مدیر"

    user_type = models.CharField(
        max_length=3, 
        default=UserTypes.SIMPLE_USER,
        choices=UserTypes.choices,
        verbose_name="نوع کاربر"
    )

    email = models.EmailField(unique=True, verbose_name="ایمیل")
    username = models.CharField(max_length=40, unique=True, verbose_name="نام کاربری")
    joined_date = models.DateField(auto_now_add=True, verbose_name="تاریخ پیوستن")
    
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="مدیر")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = managers.UserManager()

    class Meta:
        ordering = ['joined_date']
        verbose_name = "کاربر"  # Human-readable singular name in Persian
        verbose_name_plural = "کاربران"  # Human-readable plural name in Persian

    def __str__(self):
        return self.username
    
    # Required methods for admin
    def has_perm(self, perm, obj=None):
        return True  # Adjust this as needed for your permission logic

    def has_module_perms(self, app_label):
        return True  # Adjust this as needed for your permission logic

    def get_all_permissions(self, obj=None):
        # Return a set of all permissions for the user
        return set()  # Adjust this to return the actual permissions if you have any

    def get_group_permissions(self, obj=None):
        return set()  # Return any group permissions if applicable