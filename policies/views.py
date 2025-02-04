from rest_framework import viewsets
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

# ✅ Function to generate a unique policy number
def generate_policy_number():
    return uuid.uuid4().hex[:12].upper()  # 12-character unique code


@csrf_exempt
def policy_list_create_view(request):
    if request.method == 'GET':
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

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            vehicle = get_object_or_404(Vehicle, id=data.get("vehicle_id"))
            customer = vehicle.customer  # Get associated NewCustomer instance

            with transaction.atomic():
                policy = Policy.objects.create(
                    policy_number=generate_policy_number(),
                    vehicle=vehicle,
                    policy_type=data.get("policy_type"),
                    coverage_start_date=data.get("coverage_start_date"),
                    coverage_end_date=data.get("coverage_end_date"),
                    premium_amount=data.get("premium_amount"),
                    insured_value=data.get("insured_value"),
                    policy_holder=customer,
                    status="Active",
                )

            return JsonResponse({"message": "Policy created successfully.", "policy_number": policy.policy_number})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
