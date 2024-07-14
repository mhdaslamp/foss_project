# busportal/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, adm_no, password=None, **extra_fields):
        if not adm_no:
            raise ValueError('The Admission Number is required')
        user = self.model(adm_no=adm_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, adm_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(adm_no, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    adm_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'adm_no'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.adm_no

    class Meta:
        app_label = 'busportal'