from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from Profiles.models import CustomersProfile, EmployeeProfile


class UserManager(BaseUserManager):
    
    def create_user(self, username, email, user_type, password=None, password_conf=None):
        # Validate required fields
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        if password is None:
            raise ValueError('The Password field must be set')
        if password != password_conf:
            raise ValidationError('Passwords do not match')  # Ensure this raises a single string message

        # Normalize the email address
        email = self.normalize_email(email)

        # Create a new user instance
        user = self.model(
            username=username,
            email=email,
            user_type=user_type,
        )

        # Set the user's password
        user.set_password(password)
        user.save(using=self._db)  # Save the user to the database

        # Create a corresponding profile for the user
        self.create_profile(user, user_type)

        return user

    def create_superuser(self, username, email, password=None):
        # Create a superuser with admin privileges
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            user_type="ADM",  # Set user_type to 'ADM' for superuser
            password=password,
            password_conf=password  # For superuser, we can set password_conf to the same value
        )

        # Grant admin and superuser privileges
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)  # Save the superuser to the database

        return user

    def create_profile(self, user, user_type):
        # Create a profile based on the user type
        if user_type == 'CST':
            # Create or get a customer profile
            profile, created = CustomersProfile.objects.get_or_create(customer=user)
            return profile
        elif user_type == 'EMP':
            # Create or get an employee profile
            profile, created = EmployeeProfile.objects.get_or_create(employee=user)
            return profile
        return None  # Return None if user_type is not recognized