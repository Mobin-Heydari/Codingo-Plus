from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    # Method to create user with provided credentials
    def create_user(self, username, email , user_type, password=None, password_conf=None): 
        
        email = email.lower()
        
        user = self.model( 
            username = username,
            email = email,
            user_type = user_type,
        )
        
        user.set_password(password) 
        user.save(using = self._db)
        
        return user 

    # Method to create superuser with provided credentials
    def create_superuser(self, username, email, password=None):
        
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            user_type="ADM",
            password=password,
        )
        
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
