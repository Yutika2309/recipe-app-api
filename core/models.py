from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.

class UserManager(BaseUserManager):
    """
        @description: Create, save and return a new user (manage the 'User' model)
    """
    def create_user(self, email, password=None, **extra_field):
        user = self.model(email=email, **extra_field)
        user.set_password(password) #set_password encrypts the password
        user.save(using=self._db) #self._db enables multi-database support; very rare but good practice
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
        @description: User in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = "email"  #overrides the default username field of AbstractBaseUser