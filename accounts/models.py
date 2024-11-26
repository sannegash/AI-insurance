from django.db import models

from django.db import models


# Create your models here
class User(models.Model):
    # First signup user before onboarded as a customer
    # Boiler plate data
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)

    ### need to setup a type of system to preview the status of the user and how to flip to the new cutoemr page
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        db_table = 'user'
        ordering = ['last_name', 'first_name']



class NewCustomer(models.Model):
    # User who is filling out the form (link to the existing User model)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='new_customer')

    # Personal Information
    age = models.IntegerField()  # Age of the customer
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    driving_experience = models.IntegerField()  # Years of driving experience
    education = models.CharField(max_length=100)  # Education level (e.g., High School, Bachelor's, etc.)
    income = models.DecimalField(max_digits=10, decimal_places=2)  # Income, stored as a decimal (e.g., $50,000.00)

    # Vehicle-related Information
    vehicle = models.CharField(max_length=100)  # Vehicle make/model or type
    married = models.BooleanField()  # Whether the customer is married or not
    children = models.IntegerField()  # Number of children, 0 if none

    # Address and Location
    postal_code = models.CharField(max_length=20)  # Postal code
    city = models.CharField(max_length=100)  # City
    state = models.CharField(max_length=100)  # State/Province

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


class Underwriter(models.Model):
    # linked using the foriegn key of the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='underwriters')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Underwriter: {self.user.username}"


class Cashier(models.Model):
    # linked using the foriegn key of the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cashiers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cashier: {self.user.username}"


class ClaimOfficer(models.Model):
    # linked using the foriegn key of the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claim_officer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim Officer: {self.user.username}"
