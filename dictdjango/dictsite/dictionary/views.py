from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bs4 import BeautifulSoup
import requests


# Create your views here.

def index(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        url = 'https://www.dictionary.com/browse/' + word
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')
        span = soup.find_all('span', {'class': 'one-click-content'})
        context = {
            'text': span[0].text,
            'word': word
        }
        return render(request, 'dictionary/index.html', context)
    return render(request, 'dictionary/index.html')
