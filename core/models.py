from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_birth_date(value):
    today = timezone.now().date()
    age_limit = today - timedelta(days=18*365.25)
    if value > age_limit:
        raise ValidationError("You must be at least 18 years old.")


class User(AbstractUser):
    birth_date = models.DateField(validators=[validate_birth_date], null=True)
    email = models.EmailField(unique=True)

