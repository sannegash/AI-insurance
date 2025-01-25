from django.db import models
from accounts.models import NewCustomer  # Assuming NewCustomer is in the accounts subapp

class BankAccount(models.Model):
    new_customer = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, related_name="bank_accounts")
    
    # Chapa-specific fields
    account_name = models.CharField(max_length=100)  # Name of the account holder
    account_number = models.CharField(max_length=20)  # Account number (can be alphanumeric)
    bank_code = models.IntegerField()  # Recipient's bank code
    bank_name = models.CharField(max_length=100)  # Name of the bank
    reference = models.CharField(max_length=100)  # Merchant's unique reference for the transfer
    
    # Additional fields for amount, currency, etc.
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount to be transferred
    currency = models.CharField(max_length=3, default='ETB')  # Currency (Expected: ETB)
    
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the account was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the account was last updated

    def __str__(self):
        return f"Bank Account of {self.account_name} - {self.bank_name}"
