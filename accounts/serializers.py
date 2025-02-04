# serializers.py (inside your app, e.g., 'accounts')
from rest_framework import serializers
from core.models import User
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer
from vehicle.models import Vehicle, Driver
from core.serializers import UserSerializer
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'role',]


class NewCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewCustomer
        fields = [ 'age','driving_experience', 'education', 'income',
        'owner_name', 'phone_number', 'postal_code','city', 'state','status',
        'married', 'children', 'traffic_violations', 'number_of_accidents',
        'created_at', ]    
    
    def create(self, validated_data):
        # Step 1: Get the existing User instance
        user = self.context['request'].user  # Assuming 'user' is passed as part of validated_data
        validated_data['user'] = user
        
        # Step 2: Create a NewCustomer instance and attach it to the existing user
        new_customer = NewCustomer.objects.create(**validated_data)
        
        # Step 3: Return the NewCustomer instance, which is now attached to the user
        return new_customer


class UnderwriterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Underwriter
        fields = ['user', 'created_at']

class ClaimOfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClaimOfficer
        fields = ['user', 'created_at']
        
class CashierSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cashier 
        fields = ['user', 'created_at']