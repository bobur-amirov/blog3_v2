from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=50, unique=True,
                                help_text=(
                                   "Siz 50 ta belgidan iborat username tanlashingiz mumkin"
                                ),
                                error_messages={
                                    "unique": "Bunaqa user avval ruyxatdan utgan.",
                                },
                                )
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='account')
    address = models.CharField(max_length=150, null=True, blank=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
