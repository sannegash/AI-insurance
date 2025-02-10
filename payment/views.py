from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
import requests
import uuid

class MakePaymentView(APIView):

    def post(self, request, *args, **kwargs):
        # Collect data from the request
        amount = request.data.get('amount')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        callback_url = request.data.get('callback_url')
        return_url = request.data.get('return_url')
        title = request.data.get('title', 'Payment for subscription')
        description = request.data.get('description', 'I love online payments')

        if not amount or not email or not first_name or not last_name or not callback_url or not return_url:
            raise ValidationError("Missing required fields")

        tx_ref = f"tx-{uuid.uuid4()}"

        # Prepare payload for the Chapa API request
        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "tx_ref": tx_ref,
            "callback_url": callback_url,
            "return_url": return_url,
            "customization": {
                "title": title,
                "description": description
            }
        }

        headers = {
            'Authorization': 'Bearer CHAPUBK_TEST-uwf74g2tdYC7RMNF3F5RTcioNCtbOwKH',
            'Content-Type': 'application/json'
        }

        # Send the request to the Chapa API
        url = "https://api.chapa.co/v1/transaction/initialize"
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            payment = Payment.objects.create(
                amount=amount,
                currency="ETB",
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                tx_ref=tx_ref,
                callback_url=callback_url,
                return_url=return_url,
                title=title,
                description=description,
                checkout_url=data['data']['checkout_url'],
                payment_status='pending'
            )

            return Response({
                'status': 'success',
                'checkout_url': data['data']['checkout_url'],
                'tx_ref': tx_ref,
                'payment_id': payment.id
            }, status=status.HTTP_200_OK)
        
        else:
            raise ValidationError(f"Payment initialization failed. Status code: {response.status_code}")

