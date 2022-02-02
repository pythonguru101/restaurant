from rest_framework import serializers
from restaurant.models import Restaurant
from user.serializers import UserMinimalSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name")
        extra_kwargs = {
            'owner': {'read_only': True},
        }

