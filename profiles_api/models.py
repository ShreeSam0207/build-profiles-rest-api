from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, name, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.name

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    #every time a user updates their time, their feed gets updated
    #uses a foreign key relationship to a remote models
    #allows us to maintain the integrity as we cant update a feed item to a user who does not exist
    user_profile = models.ForeignKey(
    #retrieves the auth user model from settings file
        settings.AUTH_USER_MODEL,
        #what happens when we remove a user and profile feed items associated with it
        #We use cascade here to cascade down the changes and remove the associated feed items
        #another option is models.setnull to set the model to null for which the user is removed
        on_delete = models.CASCADE
        )
    status_text = models.CharField(max_length=255)
    #every time we created a new item, Automatically add the date time when the item was created
    created_on = models.DateTimeField(auto_now_add=True)

    #convert model instance to string
    def __str__(self):
        """Return the model as a string"""
        return self.status_text
