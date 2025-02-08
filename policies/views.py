from rest_framework import viewsets
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import json
import uuid

from .models import Policy
from accounts.models import NewCustomer
from vehicle.models import Vehicle
from .serializers import PolicySerializer

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user
        
        # Get the NewCustomer associated with the logged-in user
        new_customer = user.newcustomer  # Assuming `newcustomer` is a OneToOneField on the User model
        
        # Filter policies where the vehicle's customer is the logged-in user's NewCustomer
        return Policy.objects.filter(vehicle__customer=new_customer)

    # Function to generate a unique policy number
    @staticmethod
    def generate_policy_number():
        return uuid.uuid4().hex[:12].upper()  # 12-character unique code

    def perform_create(self, serializer):
        # Override the perform_create method to add the generated policy number before saving
        policy_number = self.generate_policy_number()  # Generate a unique policy number
        serializer.save(policy_number=policy_number)  # Save with the generated policy number
class CustomerListView(View):
    def get(self, request):
        try:
            customers = NewCustomer.objects.all()  # Fetch all customers

            customer_data = []
            for customer in customers:
                vehicles = Vehicle.objects.filter(customer=customer)

                # Only add customers with vehicles
                if vehicles.exists():
                    vehicle_data = [
                        {
                            "id": v.id,
                            "registration_number": v.registration_number,
                            "owner_name": v.owner_name,
                            "make": v.vehicle_make,
                            "model": v.vehicle_model,
                            "year": v.vehicle_year,
                            "fuel_type": v.fuel_type,
                            "transmission_type": v.transmission_type,
                            "engine_capacity": float(v.engine_capacity),  # Convert Decimal to float
                            "color": v.color,
                            "chassis_number": v.chassis_number,
                            "created_at": v.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                            "updated_at": v.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                        }
                        for v in vehicles
                    ]

                    customer_data.append({
                        "id": customer.id,
                        "name": customer.owner_name,
                        "email": customer.user.email,
                        "phone_number": customer.phone_number,
                        "postal_code": customer.postal_code,
                        "city": customer.city,
                        "state": customer.state,
                        "age": customer.age,
                        "driving_experience": customer.driving_experience,
                        "education": customer.education,
                        "income": float(customer.income),  # Convert Decimal to float
                        "married": customer.married,
                        "children": customer.children,
                        "traffic_violations": customer.traffic_violations,
                        "number_of_accidents": customer.number_of_accidents,
                        "status": customer.status,  # Customer status (New, Insured, Rejected)
                        "created_at": customer.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                        "vehicles": vehicle_data,  # Include vehicle details
                    })

            return JsonResponse({"customers": customer_data}, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

class PolicyCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            # Get the vehicle instance based on the vehicle_id sent in the request
            vehicle = get_object_or_404(Vehicle, chassis_number=data.get("vehicle"))


            # Get the associated customer (optional if not needed for creating the policy)
            customer = vehicle.customer  # Optional, if policy_holder is required

            with transaction.atomic():
                # Create a new policy
                policy = Policy.objects.create(
                    policy_number=generate_policy_number(),
                    vehicle=vehicle,
                    policy_type=data.get("policy_type"),
                    coverage_start_date=data.get("coverage_start_date"),
                    coverage_end_date=data.get("coverage_end_date"),
                    premium_amount=data.get("premium_amount"),
                    insured_value=data.get("insured_value"),
                    policy_holder=customer,  # Set the policy_holder if needed
                    status="Active",
                )

            return JsonResponse({"message": "Policy created successfully.", "policy_number": policy.policy_number})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)