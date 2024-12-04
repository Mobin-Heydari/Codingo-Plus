from django.db import models
from django.core.validators import EmailValidator



class Contact(models.Model):
    
    full_name = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )
    
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )
    
    email = models.EmailField(
        validators=[EmailValidator],
        blank=True,
        null=True
    )
    
    message = models.TextField(
        blank=True,
        null=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    
    def __str__(self):
        return f"{self.full_name} {self.message}"