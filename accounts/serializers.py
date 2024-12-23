# serializers.py (inside your app, e.g., 'accounts')
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import User
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'postal_code', 'city', 'state', 'status']


class NewCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = NewCustomer
        fields = ['user', 'age','driving_experience', 'education', 'income', 'married', 'children', 'traffic_violations', 'number_of_accidents','created_at']    
    
    def create(self, validated_data):
        #Handle creation of new customer instance 
        user_data = validated_data.pop('user')
        user = User.object.create(**user_data) #create the user object 
        new_customer = NewCustomer.object.create(user=user, **validated_data) #create new customer
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