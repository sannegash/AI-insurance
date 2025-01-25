import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

class MakePaymentView(View):
    @csrf_exempt
    def post(self, request):
        try:
            # Retrieve data from the request
            data = request.POST
            account_name = data.get("account_name")
            account_number = data.get("account_number")
            amount = data.get("amount")
            currency = data.get("currency", "ETB")
            reference = data.get("reference")
            bank_code = data.get("bank_code")
            
            # Prepare payload for Chapa API
            payload = {
                "account_name": account_name,
                "account_number": account_number,
                "amount": amount,
                "currency": currency,
                "reference": reference,
                "bank_code": bank_code,
            }

            # Chapa API URL
            url = "https://api.chapa.co/v1/transfers"

            # Chapa secret key
            headers = {
                'Authorization': 'CHAPUBK_TEST-uwf74g2tdYC7RMNF3F5RTcioNCtbOwKH',  # Replace with your actual secret key
                'Content-Type': 'application/json'
            }

            # Make the request to Chapa API
            response = requests.post(url, json=payload, headers=headers)

            # If the request was successful, return the response data
            if response.status_code == 200:
                return JsonResponse(response.json(), status=200)
            else:
                return JsonResponse({"error": "Transfer failed", "details": response.json()}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
