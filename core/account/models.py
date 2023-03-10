from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager ,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        """
        Creates and saves a User with the given Email , password and extra fields.
        """
        if not email:
            raise ValueError(_("the email must be set"))
        # user = self.model(phone_number=phone_number,**extra_fields)
        user = User(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        """
        Creates and saves a superuser with the given email , password and extra fields.
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_verified',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have superuser=True."))
    
        return self.create_user(email,password,**extra_fields)



# def validate_phone_number(value):
#     if  not bool(re.compile("^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$").match(value)):
#         raise ValidationError(
#             _('number is not valid'),
#         )

class User(AbstractBaseUser,PermissionsMixin):
    '''
    Custom User Model for our app
    '''
    email = models.EmailField(max_length=254,unique=True)
    full_name = models.CharField(max_length=250)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.email

