from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class SimpleUserProfile(models.Model):
    """
        Model representing a simple user profile.
    """
    
    user = models.OneToOneField(
        "Users.User",
        on_delete=models.CASCADE,
        related_name="User_Profile",
        verbose_name="کاربر"
    )
    
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام کامل")
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/simple-user-profiles/',
        null=True,
        blank=True,
        verbose_name="تصویر پروفایل"
    )
    
    bio = models.TextField(null=True, blank=True, verbose_name="بیوگرافی")

    class Meta:
        verbose_name = 'پروفایل کاربر ساده'  # Human-readable singular name in Persian
        verbose_name_plural = 'پروفایل‌های کاربران ساده'  # Human-readable plural name in Persian


class EmployeeProfile(models.Model):
    """
        Model representing an employee profile.
    """
    
    class EmployeeStack(models.TextChoices):
        """Choices for the employee's stack type."""
        DESIGNER = 'DES', 'طراح'
        DEVELOPER = 'DEV', 'توسعه‌دهنده'
        MANAGER = 'MAN', 'مدیر'
        
    employee = models.OneToOneField(
        "Users.User",
        on_delete=models.CASCADE,
        related_name="Employee_Profile",
        verbose_name="کارمند"
    )
    
    full_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="نام کامل"
    )
    
    employee_stack = models.CharField(
        max_length=3,
        default=EmployeeStack.DEVELOPER,
        choices=EmployeeStack.choices,
        blank=True,
        null=True,
        verbose_name="نوع شغل"
    )
    
    job_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="عنوان شغلی"
    )
    
    bio = models.TextField(null=True, blank=True, verbose_name="بیوگرافی")
    
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_pictures/employees-profiles/',
        verbose_name="تصویر پروفایل"
    )
    
    years_of_experience = models.PositiveIntegerField(default=1, verbose_name="سال‌های تجربه")  # Default experience is set to 1 year

    class Meta:
        verbose_name = 'پروفایل کارمند'  # Human-readable singular name in Persian
        verbose_name_plural = 'پروفایل‌های کارمندان'  # Human-readable plural name in Persian


class EmployeeSkills(models.Model):
    """
        Model representing a skill associated with an employee.
    """
    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE,
        related_name='employee_skills',
        verbose_name='کارمند'
    )
    
    skill = models.CharField(max_length=255, verbose_name="مهارت")
    
    mastery = models.IntegerField(
        validators=[
            MinValueValidator(0),  # Minimum mastery value is 0
            MaxValueValidator(100)  # Maximum mastery value is 100
        ],
        verbose_name="سطح تسلط"
    )

    class Meta:
        verbose_name = 'مهارت کارمند'  # Human-readable singular name in Persian
        verbose_name_plural = 'مهارت‌های کارمندان'  # Human-readable plural name in Persian