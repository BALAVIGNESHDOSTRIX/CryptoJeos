from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    #For getting the treding prcie
    api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,XRP,DASH,LTC,ZEC,ETC,QTUM,XMR,NEO,BCH,BCHSV,TRX,USDT,XLM,BCHABC,HSR,MITH,ADA&tsyms=USD')
    api_price_data = json.loads(api_request.content)
    #For Getting the trending news
    api_data_json  = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api_parse_data = json.loads(api_data_json.content)
    return render(request,'home.html',{'api' : api_parse_data,'price' : api_price_data})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        #For getting the treding prcie
        serach_quoate = request.POST['quote']
        serach_quoate = serach_quoate.upper()
        qoute_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + serach_quoate +'&tsyms=USD')
        quote_price_data = json.loads(qoute_request.content)
        
        return render(request,'prices.html',{'quote': serach_quoate,'searchD' : quote_price_data})
    else:
        return render(request,'prices.html',{'notfound' : "NotFound"})

    