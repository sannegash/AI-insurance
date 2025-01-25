# serializers.py (inside your app, e.g., 'accounts')
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import User
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer
from vehicle.models import Vehicle, Driver
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

class CombinedCustomerDataSerializer(serializers.Serializer):
    # Personal info (from the Account model)
    owner_name = serializers.CharField(max_length=255)
    driving_experience = serializers.IntegerField()
    education = serializers.CharField(max_length=255)
    income = serializers.DecimalField(max_digits=10, decimal_places=2)
    postal_code = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)

    # Vehicle info (from the Vehicle model)
    vehicle_make = serializers.CharField(max_length=100)
    vehicle_model = serializers.CharField(max_length=100)
    vehicle_year = serializers.IntegerField()
    fuel_type = serializers.CharField(max_length=50)
    transmission_type = serializers.CharField(max_length=50)
    engine_capacity = serializers.DecimalField(max_digits=5, decimal_places=2)
    chassis_number = serializers.CharField(max_length=50)

    # Driver info (from the Driver model)
    driver_first_name = serializers.CharField(max_length=100)
    driver_last_name = serializers.CharField(max_length=100)
    driver_license_number = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # Here we save the data to the respective models
        account_data = {
            'owner_name': validated_data['owner_name'],
            'driving_experience': validated_data['driving_experience'],
            'education': validated_data['education'],
            'income': validated_data['income'],
            'postal_code': validated_data['postal_code'],
            'city': validated_data['city'],
            'state': validated_data['state'],
            'phone_number': validated_data['phone_number'],
        }
        account = Account.objects.create(**account_data)

        vehicle_data = {
            'account': account,
            'vehicle_make': validated_data['vehicle_make'],
            'vehicle_model': validated_data['vehicle_model'],
            'vehicle_year': validated_data['vehicle_year'],
            'fuel_type': validated_data['fuel_type'],
            'transmission_type': validated_data['transmission_type'],
            'engine_capacity': validated_data['engine_capacity'],
            'chassis_number': validated_data['chassis_number'],
        }
        vehicle = Vehicle.objects.create(**vehicle_data)

        driver_data = {
            'account': account,
            'driver_first_name': validated_data['driver_first_name'],
            'driver_last_name': validated_data['driver_last_name'],
            'driver_license_number': validated_data['driver_license_number'],
        }
        driver = Driver.objects.create(**driver_data)

        return account 

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