from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=MLN,REP,GNO,APH,ING,DAT,FOTA&tsyms=ETH")
    price = json.loads(price_request.content)
    return render(request, 'home.html', {'price': price})


def cryptonews(request):
    import requests
    import json
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'cryptonews.html', {'api': api})

def ethpairs(request):
    import requests
    import json
    ethpairs_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=MLN,REP,GNO,APH,ING,DAT,FOTA&tsyms=ETH")
    ethpairs = json.loads(ethpairs_request.content)
    return render(request, 'ethpairs.html', {'ethpairs': ethpairs})

def btcpairs(request):
    import requests
    import json
    btcpairs_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ERC,ETH,ETC,EDG,EOS,PART,WAVES,XRP,XLM,XMR,ADA,XEM,BCH&tsyms=BTC")
    btcpairs = json.loads(btcpairs_request.content)
    return render(request, 'btcpairs.html', {'btcpairs': btcpairs})


def usdpairs(request):
    import requests
    import json
    usdpairs_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,ETC,LTC,EOS,XRP,XLM,BCH,XMR,ADA,XEM&tsyms=USD")
    usdpairs = json.loads(usdpairs_request.content)
    return render(request, 'usdpairs.html', {'usdpairs': usdpairs})

def cryptolookup(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        cryptolookup_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=BTC,USD,ETH")
        cryptolookup = json.loads(cryptolookup_request.content)
        return render(request, 'cryptolookup.html', {'quote' :quote, 'cryptolookup': cryptolookup})

    else:
        return render(request, 'cryptolookup.html', {})