from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    address = models.CharField(max_length=200)

    shipping_city = models.CharField(max_length=60)
    shipping_country = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=50)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

