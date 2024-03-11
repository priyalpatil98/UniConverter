from django.http import JsonResponse
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request,'index.html')

def convert(request):
    context = {}
    print(request)

    if 'currency_submit' in request.POST:
        source_currency = request.POST.get('source_currency')
        amount = request.POST.get('amount')
        target_currency = request.POST.get('target_currency')

        context['currency_result'] = currency_converter(source_currency, amount, target_currency)

    elif 'language_submit' in request.POST:
        text = request.POST.get('text')
        to = request.POST.get('to')
        from1 = request.POST.get('from')

        context['language_result'] = language_converter(text, to, from1)
        
    return render(request, 'currency_converter.html', context)

def currency_converter(source_currency, amount, target_currency):

        api_url = "https://w7u4eh9pg1.execute-api.eu-west-2.amazonaws.com/PROD/x22209573_currency_converter"

        params = {
            'source_currency': source_currency,
            'amount': amount,
            'target_currency': target_currency
        }

        try:
            response = requests.post(api_url, params=params)

            if response.status_code == 200:
                result = response.json()
                return result
            else:
                error = 'API request failed with status code {}'.format(response.status_code)
                return error
        
        except Exception as e:
            error = 'Failed to connect to the API. Try Again!'

def language_converter(text, to, from1):        

        api = "https://v8aeftpa0i.execute-api.us-west-2.amazonaws.com/default/x2213868Translate"

        params = {
            'text': text,
            'to': to,
            'from': from1
        }

        try:
            response = requests.post(api, json=params)

            if response.status_code == 200:
                result = response.json()
                return result
            else:
                error = 'API request failed with status code {}'.format(response.status_code)
                return error
        
        except Exception as e:
            error = 'Failed to connect to the API. Try Again!'
