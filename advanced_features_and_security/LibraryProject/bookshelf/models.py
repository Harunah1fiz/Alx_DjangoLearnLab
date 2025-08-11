from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom manager for our CustomUser Model.
    Inherits from BaseUserManager, which has helper methods like normalize_email().
    """
    
    def create_user(self, username, email, password=None,  **extra_fields):
        """
        Creates and returns a regular user.
        - username: required
        - email: required
        - password: optional but usually provided
        - extra_fields: any other model fields (e.g., phone_number, date_of_birth)
        """

        if not email:
            raise ValueError("User must have an email address")
        
        # Ensures email is lowercase and cleaned
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using= self.db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a superuser (admin).
        Ensures they have staff and superuser privileges.
        """

        # Force these fields to True for superusers
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Validation checks
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Use create_user to avoid repeating code
        return self.create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null= True)
    profile_photo = models.ImageField()

    objects = CustomUserManager()

    def __str__(self):
        return self.username






class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


