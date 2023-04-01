from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import AccountManger
from lib.mixins import NULL
from uuid import uuid4


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, **NULL)

    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=30, unique=True, **NULL)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    objects = AccountManger()

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
