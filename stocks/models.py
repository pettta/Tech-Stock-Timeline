from django.db import models
import yfinance as yf 

class stock_data(models.Model):  
  stock_name = models.CharField(max_length=30)
  ticker = models.CharField(max_length=4)
  
  def __str__(self):
    return self.stock_name
  
  def stock_info(self):
    ticker = self.ticker
    return yf.Ticker(ticker)

  def stock_volume(self):
    week_history = self.stock_info().history(period='1wk')
    closest_volume = week_history['Volume'][4]   
    return closest_volume

  def getTicker(self):
    return self.ticker