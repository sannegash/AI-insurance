from django.db import models

# Create your models here.
class RiskAssessment (models.Model):
     # AI prediction
    risk_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Predicted risk score from the AI.")
    recommendation = models.TextField(blank=True, help_text="AI's recommendation based on risk score.")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return f"Risk Assessment for {self.user.username} - {self.policy_type}"
