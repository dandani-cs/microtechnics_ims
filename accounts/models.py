from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date
import random

class User(AbstractUser):
    def generate_id():
        return str(date.today().year) + str(random.randint(100000, 999999))

    # username becomes employeeID
    username = models.CharField(max_length=10, primary_key=True, unique=True, default=generate_id)
    email = models.EmailField(max_length=254, unique=True, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    is_admin = models.BooleanField(default=False)
