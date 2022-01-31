from django.db import models
from core.base_model import BaseModel
# Create your models here.


class Restaurant(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Menu(BaseModel):
    restaurant = models.ForeignKey(Restaurant, related_name="menus", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)
