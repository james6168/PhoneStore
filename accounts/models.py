import uuid

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User should have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staff_user(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True, verbose_name="email address")
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    token = models.CharField(default=uuid.uuid4(), max_length=36)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()

