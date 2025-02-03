from django.db import models
from vehicle.models import Vehicle
from django.contrib.auth import get_user_model
from accounts.models import NewCustomer
User = get_user_model()


class Policy(models.Model):
    POLICY_TYPE_CHOICES = [
        ('Comprehensive', 'Comprehensive'),
        ('Third-Party', 'Third-Party'),
        ('Third-Party, Fire and Theft', 'Third-Party, Fire and Theft'),
    ]

    policy_number = models.CharField(max_length=20, unique=True, help_text="Unique policy number.", editable= False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="policies", help_text="Vehicle covered by this policy.")
    policy_type = models.CharField(max_length=30, choices=POLICY_TYPE_CHOICES, help_text="Type of insurance policy.")
    coverage_start_date = models.DateField(help_text="Start date of the coverage.")
    coverage_end_date = models.DateField(help_text="End date of the coverage.")
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="The premium amount for the policy.")
    insured_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="The value of the vehicle insured under this policy.")
    policy_holder = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name="policies", help_text="The policyholder (user who owns the policy).")
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Cancelled', 'Cancelled')], default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Policy {self.policy_number} for {self.insured_name}"

    def is_active(self):
        from datetime import date
        return self.coverage_start_date <= date.today() <= self.coverage_end_date



