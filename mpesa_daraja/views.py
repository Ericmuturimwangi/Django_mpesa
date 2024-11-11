from django.shortcuts import render
from django.http import JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    try:
        cl = MpesaClient()
        phone_number = '0720630112'
        amount = 1
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'
        
        # Perform the STK push request
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        # If the response is an object that is not directly serializable to JSON
        # You can try converting it to a dictionary or JSON response format
        if hasattr(response, 'response'):
            response_data = response.response  # Assuming the response has a 'response' attribute
        else:
            response_data = response  # If it's already in a format you can use

        # Return a JSON response
        return JsonResponse(response_data, safe=False)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)