from django.db import models
from core.models import User 

# Custom validator for claim likelihood
def validate_claim_likelihood(value):
    if not (0 <= value <= 100):
        raise ValidationError("Claim likelihood must be between 0 and 100.")

class RiskAssessment (models.Model):
   insuredcustomer = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="riskassessment"
    )
   #Enum choices for risk_factor
   RISK_FACTORS = [ 
      ('High', 'High'), 
      ('Medium', 'Medium'),
      ('Low', 'Low'),
   ]
     # AI prediction
   risk_factor = models.CharField(
      max_length=6,
      choices= RISK_FACTORS, 
      default='Medium',
      help_text="Predicted risk score from the AI.")

   claim_likelihood = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      validators=[validate_claim_likelihood]     
    )

    # Metadata
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f"Risk Assessment for {self.user.username} - {self.policy_type}"
