# serializers.py (inside your app, e.g., 'accounts')
from rest_framework import serializers
from core.models import User
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer
from vehicle.models import Vehicle, Driver
from vehicle.serializers import VehicleSerializer, DriverSerializer
from core.serializers import UserSerializer
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'role',]


class NewCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    Vehicle = VehicleSerializer(many=True)  # Include vehicles (many-to-many relationship)

    class Meta:
        model = NewCustomer
        fields = ['user', 'age','driving_experience', 'education', 'income','owner_name', 'phone_number', 'postal_code','city', 'state','married', 'children', 'traffic_violations', 'number_of_accidents','created_at','Vehicle', ]    
    
    def create(self, validated_data):
        #Handle creation of new customer instance 
        user_data = validated_data.pop('user')
        user = User.object.create(**user_data) #create the user object 
        new_customer = NewCustomer.object.create(user=user, **validated_data) #create new customer
        return new_customer

class CombinedCustomerDataSerializer(serializers.Serializer):
    chassis_number = serializers.CharField(max_length=255)
    owner_name = serializers.CharField(max_length=255)
    vehicle_make = serializers.CharField(max_length=255)
    vehicle_year = serializers.IntegerField()
    fuel_type = serializers.CharField(max_length=255)
    transmission_type = serializers.CharField(max_length=255)
    engine_capacity = serializers.FloatField()
    color = serializers.CharField(max_length=255)
    driver_firstname = serializers.CharField(max_length=255)
    driver_lastname = serializers.CharField(max_length=255)
    driver_license_number = serializers.CharField(max_length=255)
    customer_id = serializers.IntegerField()  # Assuming `NewCustomer` is linked with an ID

    def validate(self, data):
        # Check if NewCustomer exists
        if not NewCustomer.objects.filter(id=data['customer_id']).exists():
            raise serializers.ValidationError("Customer with the given ID does not exist.")
        return data




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