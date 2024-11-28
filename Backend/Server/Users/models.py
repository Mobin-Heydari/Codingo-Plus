from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from . import managers


class User(AbstractBaseUser):
    
    class UserTypes(models.TextChoices):
        CUSTOMER = "CST", "Customer"
        EMPLOYEE = "EMP", "Employee"
        ADMIN = "ADM", "Admin"

    user_type = models.CharField(
        max_length=3, 
        default=UserTypes.CUSTOMER,
        choices=UserTypes.choices,
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    joined_date = models.DateField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = managers.UserManager()
    class Meta:
        ordering = ['joined_date']
        verbose_name = "User "
        verbose_name_plural = "Users"

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