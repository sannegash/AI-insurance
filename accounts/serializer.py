# serializers.py (inside your app, e.g., 'accounts')
from django.contrib.auth.models import User
from rest_framework import serializers

class CustomerSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming you're using Django's built-in User model
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        # Create user, can also add more logic to handle passwords
        user = User.objects.create_user(**validated_data)
        
        # Send an email to the admin with the new sign-up details
        self.send_new_signup_email(user)
        
        return user

    def send_new_signup_email(self, user):
        # Send email to admin on new signup
        from django.core.mail import send_mail
        from django.conf import settings
        
        admin_email = settings.ADMIN_EMAIL  # Make sure to configure an admin email
        subject = f"New Customer Signup: {user.username}"
        message = f"A new customer has signed up:\n\nUsername: {user.username}\nEmail: {user.email}\n"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])


class StaffSignupSerializer(serializers.ModelSerializer):
    ROLE_CHOICES = [ 
        ('Underwriter', 'Underwriter'),
        ('Cashier', 'Cashier'),
        ('ClaimOfficer', 'ClaimOfficer'),
    ]
    role = serializer.ChoiceField(choices=ROLE_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = { 
            'password': {'write_only': True}
        }
    def create(self ,validate_data):

        role = validate_data.pop('role')

        user = User.object.create_user(
            username=validate_date['username'],
            email=validate_datea['email'],
            password=validate_date['password']
        )

        user.profile.role = role
        user.profile.save()

        return user 
 