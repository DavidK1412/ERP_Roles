from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from securityApp.models import Permission, Role

import uuid


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField('Username', max_length=255, unique=True)
    password = models.CharField('Password',max_length=255)
    user_permissions = models.ManyToManyField(Permission, related_name='users')
    roles = models.ManyToManyField(Role, related_name='users')

    def save(self, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
