from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from Users.models import User





class CustomersProfile(models.Model):
    customer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Customer_Profile"
    )
    
    full_name = models.CharField(max_length=255, null=True, blank=True)
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/customers-profiles/',
        null=True,
        blank=True
    )
    
    bio = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'



class EmployeeSkils(models.Model):
    skill = models.CharField(max_length=255)
    
    mastery = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    
    class Meta:
        verbose_name = 'Employee Skill'
        verbose_name_plural = 'Employee Skills'


class EmployeeProfile(models.Model):
    
    class EmployeeStack(models.TextChoices):
        DESIGNER = 'DES', 'Designer'
        DEVELOPER = 'DEV', 'Developer'
        MANAGER = 'MAN', 'Manager'
        
    employee = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Employee_Profile"
    )
        
    
    employee_stack = models.CharField(
        max_length=3,
        default=EmployeeStack.DEVELOPER,
        choices=EmployeeStack.choices,
    )
    
    job_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    bio = models.TextField(null=True, blank=True)
    
    
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_pictures/employees-profiles/'
    )
    
    skils = models.ManyToManyField(
        EmployeeSkils,
        blank=True,
        related_name='employee_skills',
    )
    
    years_of_experience = models.PositiveIntegerField(default=1)
    
    
    class Meta:
        verbose_name = 'Employee Profile'
        verbose_name_plural = 'Employee Profiles'