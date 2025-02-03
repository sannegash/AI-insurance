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
        # Get customers who have vehicles
        customers = NewCustomer.objects.filter(Vehicle__isnull=False).distinct()

        customer_data = []
        for customer in customers:
            # Get the vehicles associated with each customer using the 'customer' ForeignKey
            vehicles = Vehicle.objects.filter(customer=customer)
            vehicle_data = [{"id": v.id, "plate_number": v.registration_number, "make": v.vehicle_make, "model": v.vehicle_model} for v in vehicles]

            customer_data.append({
                "id": customer.id,
                "name": customer.owner_name,
                "email": customer.user.email,
                "vehicles": vehicle_data,
            })

        return JsonResponse({"customers": customer_data}, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            vehicle = get_object_or_404(Vehicle, id=data.get("vehicle_id"))
            customer = vehicle.customer  # Use 'customer' to get the associated NewCustomer instance

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
