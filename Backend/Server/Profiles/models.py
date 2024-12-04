from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class SimpleUserProfile(models.Model):
    
    """
        Model representing a simple user profile.
    """
    
    user = models.OneToOneField(
        "Users.User",
        on_delete=models.CASCADE,
        related_name="Customer_Profile"
    )
    
    full_name = models.CharField(max_length=255, null=True, blank=True)
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/simple-user-profiles/',
        null=True,
        blank=True
    )
    
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Simple User Profile'
        verbose_name_plural = 'Simple User Profiles'



class EmployeeProfile(models.Model):
    
    """
        Model representing an employee profile.
    """
    
    class EmployeeStack(models.TextChoices):
        """Choices for the employee's stack type."""
        DESIGNER = 'DES', 'Designer'
        DEVELOPER = 'DEV', 'Developer'
        MANAGER = 'MAN', 'Manager'
        
    employee = models.OneToOneField(
        "Users.User",
        on_delete=models.CASCADE,
        related_name="Employee_Profile"
    )
    
    full_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    employee_stack = models.CharField(
        max_length=3,
        default=EmployeeStack.DEVELOPER,
        choices=EmployeeStack.choices,
        blank=True,
        null=True
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
    
    years_of_experience = models.PositiveIntegerField(default=1)  # Default experience is set to 1 year

    class Meta:
        verbose_name = 'Employee Profile'
        verbose_name_plural = 'Employee Profiles'
        


class EmployeeSkills(models.Model):
    
    """
        Model representing a skill associated with an employee.
    """
    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE,
        related_name='employee_skills',
    )
    
    skill = models.CharField(max_length=255)
    
    mastery = models.IntegerField(
        validators=[
            MinValueValidator(0),  # Minimum mastery value is 0
            MaxValueValidator(100)  # Maximum mastery value is 100
        ]
    )

    class Meta:
        verbose_name = 'Employee Skill'
        verbose_name_plural = 'Employee Skills'