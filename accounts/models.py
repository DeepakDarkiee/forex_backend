from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from rest_framework_simplejwt.tokens import RefreshToken
from journal.base_model import BaseModel
# Create your models here.
from django.contrib.postgres.fields import ArrayField

class UserManager(BaseUserManager):
    
    def create_user(
        self,
        username,
        email,
        first_name=None,
        auth_provider="email",
        is_verified=False,
        password=None,
    ):
        if username is None:
            raise TypeError("User should have a username")
        user = self.model(
            username=username,
            first_name=first_name,
            is_verified=is_verified,
            auth_provider=auth_provider,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username,
        email,
        first_name=None,
        auth_provider="email",
        is_verified=True,
        password=None,
    ):
        if password is None:
            raise TypeError("Password should not be None")

        user = self.create_user(
            username,
            email,
            first_name=username,
            auth_provider="email",
            is_verified=True,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {"google": "google", "email": "email"}

ROLE_CHOICES = (
    ("Author", "Author"),
    ("Editor", "Editor"),
    ("Reviewer", "Reviewer"),
    ("Both-ER", "Both-ER"),
    ("Subscriber", "Subscriber"),
)


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(
        max_length=255, unique=True, db_index=True, null=True, blank=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(blank=True, upload_to="profile_pics",null=True)
    auth_provider = models.CharField(
        max_length=255, blank=False, null=False, default="email"
    )
    role = models.ForeignKey("Role",on_delete=models.DO_NOTHING,null=True,blank=True)
    permissions = models.TextField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class Role(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    permissions = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name