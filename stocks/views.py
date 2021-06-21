from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from .models import stock_data
from stocks.GN import newsList
import math
import pandas as pd

class IndexView(generic.ListView):
  template_name = 'stocks/index.html'
  context_object_name = 'latest_ticker_list'

  def get_queryset(self):
    return stock_data.objects.all()
  
def aboutPage(request):
  return render(request, 'stocks/about.html')

def detail(request, stock_id):
    stock_ticker = stock_data.objects.get(pk=stock_id).getTicker()
    stock_history = stock_data.objects.get(pk=stock_id).stock_info().history(period='max',interval='1d')  # Creates and gets the history for a yfinance object
    df = pd.DataFrame(stock_history['Close'].items())
    df1 = df.dropna().set_index(1) # Uses a pandas dataframe in order to avoid nan values
    stock_information = df1.itertuples()  # Stores that formatted data in a single variable / map 
    title = stock_data.objects.get(pk=stock_id).ticker
    todayDate = df1.iloc[-1][0]
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # checks if AJAX request, .is_ajax() deprecated
        news = request.POST.get('dateOfClick')  # Gets the post data from the AJAX function in detail.html
        newsListings = newsList(news, news, stock_ticker)
        return JsonResponse({'newsList': newsListings}, status=200)
    return render(request, 'stocks/detail.html',
                  {'stock_information': stock_information, 'title': title, 'currentDate': todayDate})