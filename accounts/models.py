from django.db import models
from core.models import User 
from django.db import models

class NewCustomer(models.Model):
    # Personal Information
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='newcustomer')
    age = models.IntegerField()  # Age of the customer
    driving_experience = models.IntegerField()  # Years of driving experience
    education = models.CharField(max_length=100)  # Education level (e.g., High School, Bachelor's, etc.)
    income = models.DecimalField(max_digits=10, decimal_places=2)  # Income, stored as a decimal (e.g., $50,000.00)

    # Vehicle-related Information
    married = models.BooleanField()  # Whether the customer is married or not
    children = models.IntegerField()  # Number of children, 0 if none

    
    # Traffic-related Information
    traffic_violations = models.IntegerField()  # Number of traffic violations within the last year
    number_of_accidents = models.IntegerField()  # Number of accidents in the past

    # Timestamp of form submission
    created_at = models.DateTimeField(auto_now_add=True)  # Time when the customer filled out the form

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - New Customer Info"

    class Meta:
        db_table = 'new_customer'  # Optional, you can specify a custom table name if needed
        verbose_name = 'New Customer'
        verbose_name_plural = 'New Customers'

# Create your models here

class Underwriter(models.Model):
    # linked using the one to one of the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='underwriters')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Underwriter: {self.user.username}"


class Cashier(models.Model):
    # linked using the one to one of the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cashiers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cashier: {self.user.username}"


class ClaimOfficer(models.Model):
    # linked using the one to one of the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='claim_officer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim Officer: {self.user.username}"
 