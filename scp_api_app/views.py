from django.http import JsonResponse
from django.shortcuts import render
import requests
import datetime


# Create your views here.
def index(request):
    return render(request,'index.html')

def convert(request):
    context = {}
    
    if 'currency_submit' in request.POST:
        source_currency = request.POST.get('source_currency')
        amount = request.POST.get('amount')
        target_currency = request.POST.get('target_currency')

        print(request.POST)

        context['currency_result'] = currency_converter(source_currency, amount, target_currency)
        print([context])

    elif 'language_submit' in request.POST:
        text = request.POST.get('text')
        to = request.POST.get('to')
        from1 = request.POST.get('from')

        context['language_result'] = language_converter(text, to, from1)
        
    return render(request, 'currency_converter.html', context)

def currency_converter(source_currency, amount, target_currency):

        #api_url = "https://w7u4eh9pg1.execute-api.eu-west-2.amazonaws.com/PROD/x22209573_currency_converter"

        api_url = "https://f44dxfgsya.execute-api.eu-west-2.amazonaws.com/default/convert"

        params = {
            'source_currency': source_currency,
            'amount': amount,
            'target_currency': target_currency
        }

        try:
            response = requests.post(api_url, json=params)

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

def crypto_rates(request):
     
     context = {}
     
     url= "https://api.coingecko.com/api/v3/simple/price"

     params = {
        'ids': 'bitcoin,ethereum,monero,tether,litecoin,dogecoin',
        'vs_currencies': 'usd,eur,inr,gbp',
    }
     
     try: 
          response = requests.get(url, params=params)
          response.raise_for_status()

          context['crypto_rates'] = response.json()
          
     except request.RequestException as e:
          context['error'] = str(e)
     
     return render(request, 'crypto.html', context)

def stocks_rates(request):
     
     context = {}

     base_url = 'https://www.alphavantage.co/query'
     api_key = 'BLNVJMOHI1QWSINN'

     prices = {}
     current_date = datetime.date.today()

     stocks = {
        'GOOGL': 'NASDAQ',  # Example for New York Exchange
        'RELIANCE.BSE': 'BSE',  # Example for Bombay Stock Exchange
        'TCS.NSE': 'NSE',  # Example for National Stock Exchange of India
        'AAPL': 'NASDAQ',  # Another example for New York Exchange
        'CRH.IR': 'Euronext Dublin',  # Example for a European exchange (Ireland)
    }
     
     for symbol, exchange in stocks.items():
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': api_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            prices[symbol] = {
                'price': data["Time Series (Daily)"][current_date]["1. open"],
                'exchange': exchange
            }
            context['stocks_rates'] = data
    
     return render(request, 'stocks.html', context)

