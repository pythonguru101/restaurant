from django.db import models
from django.contrib.auth.models import AbstractUser
from core.base_model import BaseModel
from user.enums import RoleChoice
# Create your models here.


class User(BaseModel, AbstractUser):
    role = models.CharField(max_length=100, choices=RoleChoice.choices, default=RoleChoice.ADMIN.value)

    def __str__(self):
        return str(self.id)
