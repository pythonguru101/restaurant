from django.db import models


class RoleChoice(models.TextChoices):
    ADMIN = "admin", "Admin"
    EMPLOYEE = "employee", "Employee"
    OWNER = "owner", "Owner"