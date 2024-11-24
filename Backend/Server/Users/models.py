from django.contrib.auth.models import AbstractBaseUser
from django.db import models


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


    class Meta:
        ordering = ['joined_date']
        verbose_name = "User "
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username