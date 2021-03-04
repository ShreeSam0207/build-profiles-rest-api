# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have a valid email address")
        email=self.normalize(email) #normalising email to handle case sesitivity
        user=self.model(email=email,name=name)

        user.set_password(password) #setting the password to hashed value
        user.save(using=self._db) #standard procedure for saving objects in Django

        return user

    def create_superuser(self,email,none,password):
        """New Suprtviser with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True #this is by default given by PermissionMixin
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELD_LIST=['name']

    def get_full_name(self):
        """Retieve full name of the user"""
        return self.name

    def get_short_name(self):
        """"Retrieve short name of the user"""
        return self.name

    def ___str__(self):
        """Return String reporesentation of the user"""
        return self.email
