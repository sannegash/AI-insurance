from django.db import models

from django.db import models
from accounts.models import NewCustomer

class Vehicle(models.Model):
    FUEL_TYPE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    TRANSMISSION_TYPE_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    customer = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name="Vehicle")
    registration_number = models.CharField(max_length=15, unique=True, help_text="Unique vehicle registration number.")
    owner_name = models.CharField(max_length=100, help_text="Name of the vehicle owner.")
    vehicle_make = models.CharField(max_length=50, help_text="Brand of the vehicle (e.g., Toyota).")
    vehicle_model = models.CharField(max_length=50, help_text="Model of the vehicle (e.g., Corolla).")
    vehicle_year = models.PositiveIntegerField(help_text="Year the vehicle was manufactured.")
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, help_text="Fuel type of the vehicle.")
    transmission_type = models.CharField(max_length=10, choices=TRANSMISSION_TYPE_CHOICES, help_text="Transmission type of the vehicle.")
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, help_text="Engine capacity in liters (e.g., 2.0 for a 2000cc engine).")
    color = models.CharField(max_length=30, help_text="Color of the vehicle.")
    chassis_number = models.CharField(max_length=50, unique=True, help_text="Unique identifier for the vehicle's chassis.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the vehicle was added.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the vehicle was last updated.")

    def __str__(self):
        return f"{self.vehicle_make} {self.vehicle_model} ({self.registration_number})"


class Driver(models.Model):
    #Driver may be employer of the insured so need to figure out logic !!
     vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name = "driver")
     driver_firstname = models.CharField(max_length=100, help_text = " first name of driver ")
     driver_lastname = models.CharField(max_length=100, help_text = " last name of driver ")
     licence_number = models.CharField(max_length=15, unique=True, help_text = "drivers licence number")









