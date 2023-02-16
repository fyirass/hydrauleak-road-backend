from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Creates and saves a User with the given email and password
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # Creates and saves a superuser with the given email and password
        user = self.create_user(email, password)
        user.roles = "is_admin"
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    roles = models.CharField(max_length=255, default="is_client", choices=(("is_admin", "is_admin"), ("is_leaker", "is_leaker"), ("is_client", "is_client")))
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        return self.roles == "is_admin"
