from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
    )
from .managers import CustomUserManager

# Create your models here.

# User Types
class UserType(models.Choices):
    MEDICAL_PRACTITIONER = "medical_practitioner"
    PATIENT = "patient"


# Custom User
class CustomUser(AbstractBaseUser,PermissionsMixin):

    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240, null=True,blank=True)
    email = models.EmailField(unique=True, max_length=254)
    user_type = models.CharField(choices= UserType.choices, max_length=240)
    is_staff = models.BooleanField(
        default=False
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(
        default=True
    )  # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
