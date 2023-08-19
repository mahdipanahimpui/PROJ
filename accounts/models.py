from django.db import models
from . managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=128, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True, max_length=128, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    # username_field and password(by default) is used to create user

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin # just availabel by superuser