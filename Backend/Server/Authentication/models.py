from django.db import models
from django.utils import timezone



class OneTimePassword(models.Model):
    # Enum for OTP status using Django's TextChoices
    class OtpStatus(models.TextChoices):
        EXPIRED = 'EXP', 'Expired'  # Represents an expired OTP
        ACTIVE = 'ACT', 'Active'      # Represents an active OTP
    
    # Field to store the status of the OTP (active or expired)
    status = models.CharField(
        max_length=3,
        choices=OtpStatus.choices,
        default=OtpStatus.ACTIVE  # Default status is active
    )
    
    # Field to store the user's email address
    email = models.EmailField()
    
    # Unique token field for the OTP
    token = models.CharField(
        max_length=250,
        unique=True  # Ensures that each token is unique
    )
    
    # Field to store the OTP code (usually a numeric string)
    code = models.CharField(max_length=6)
    
    # Field to store the expiration time of the OTP
    expiration = models.DateTimeField(
        blank=True,
        null=True,
    )
    
    # Field to store the creation time of the OTP record
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "One-Time Password"  # Human-readable singular name
        verbose_name_plural = "One-Time Passwords"  # Human-readable plural name
        
    # String representation of the OTP model
    def __str__(self):
        return f'{self.status}----{self.code}----{self.token}'
    
    # Method to calculate and set the expiration time of the OTP
    def get_expiration(self):
        created = self.created  # Get the creation time
        expiration = created + timezone.timedelta(minutes=2)  # Set expiration to 1 minute after creation
        self.expiration = expiration  # Update the expiration field
        self.save()  # Save the changes to the database
        
    # Method to validate the status of the OTP based on its expiration
    def status_validation(self):
        if self.expiration <= timezone.now():  # Check if the OTP has expired
            self.status = 'EXP'  # Set status to expired
            return self.status
        else:
            return self.status  # Return the current status