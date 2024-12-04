from django.db import models
from django.core.validators import EmailValidator



class Contact(models.Model):
    
    full_name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="نام کامل"
    )
    
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        verbose_name="شماره تلفن"
    )
    
    email = models.EmailField(
        validators=[EmailValidator],
        blank=True,
        null=True,
        verbose_name="ایمیل"
    )
    
    message = models.TextField(
        blank=True,
        null=True,
        verbose_name="پیام"
    )
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    
    class Meta:
        verbose_name = "تماس"  # Human-readable singular name in Persian
        verbose_name_plural = "تماس‌ها"  # Human-readable plural name in Persian

    
    def __str__(self):
        return f"{self.full_name} {self.message}"