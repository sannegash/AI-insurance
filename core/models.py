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
    # First signup user before onboarded as a customer
    # Boiler plate data
    CASHIER = "cashier"
    CLAIM_OFFICER = "claim_officer"
    UNDERWRITER = "underwriter"
    NEW_CUSTOMER = "new_customer"

    ROLE_CHOICES = [
        (CASHIER, "Cashier"),
        (CLAIM_OFFICER, "Claim Officer"),
        (UNDERWRITER, "Underwriter"),
        (NEW_CUSTOMER, "New Customer"),  
    ]

    username = models.CharField(max_length=150, unique=True)
    birth_date = models.DateField(validators=[validate_birth_date], null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='new_customer')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False, max_length=255)

    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    # Address and Location
    ### need to setup a type of system to preview the status of the user and how to flip to the new cutoemr page
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        db_table = 'user'
        ordering = ['last_name', 'first_name']

