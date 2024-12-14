from django.db import models
from django.db import models
from django.db import models
from vehicle.models import Vehicle
from django.contrib.auth import get_user_model
from core.models import User
from accounts.models import InsuredCustomer

class Claim(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Closed', 'Closed'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='claims')
    claimant = models.ForeignKey(InsuredCustomer, on_delete=models.CASCADE, related_name='claims')
    claim_date = models.DateField(auto_now_add=True)
    accident_date = models.DateField(help_text="Date of the accident.")
    accident_location = models.CharField(max_length=200, help_text="Where the accident occurred.")
    description = models.TextField(help_text="Detailed description of the accident and claim.")
    estimated_damage_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Estimated cost of damages.")
    police_report_number = models.CharField(max_length=50, null=True, blank=True,
                                            help_text="Police report reference, if applicable.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    claim_officer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='handled_claims',
        null=True,
        blank=True,
        help_text="The officer assigned to this claim."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim {self.id} for Vehicle {self.vehicle.registration_number}"
