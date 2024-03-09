from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def currency_converter(request):

    context = {}

    if request.method == 'GET' and 'source_currency' in request.GET and 'amount' in request.GET and 'target_currency' in request.GET:
        source_currency = request.GET['source_currency']
        amount = request.GET['amount']
        target_currency = request.GET['target_currency']

        api_url = "https://w7u4eh9pg1.execute-api.eu-west-2.amazonaws.com/PROD/x22209573_currency_converter"

        params = {
            'source_currency': source_currency,
            'amount': amount,
            'target_currency': target_currency
        }

        try:
            response = requests.get(api_url, params=params)

            if response.status_code == 200:
                context['data'] = response.json()
            else:
                context['error'] = 'API request failed with status code {}'.format(response.status_code)
        
        except Exception as e:
            context['error'] = 'Failed to connect to the API. Try Again!'
        
    return render(request, 'currency_converter.html', context)
    
