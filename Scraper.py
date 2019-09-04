# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:09:56 2019

@author: jeren
"""
import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import datetime
import os
import csv

def get_stocks_to_watch():
    """ Searches SeekingAlpha, Bloomberg and CNBC for their predictions on stocks likely to make moves that day
    Args: website names
    Returns: List of the specific stocks to watch (in their ticker symbols)
    
    
    """""
    they_say = []
    driver = webdriver.Chrome
    driver.get('https://seekingalpha.com/')
    Top_Gainers = driver.find_element_by_name('Top Gainers')
    return they_say
    
names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
Yahoo = "https://finance.yahoo.com/most-active"
r=requests.get(Yahoo)
data=r.text
soup=BeautifulSoup(data)
 
for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
   for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
   for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
   for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
   for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
   for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
   for totalVolume in listing.find_all('td', attrs={'aria-label':'Avg vol (3-month)'}):
      totalVolumes.append(totalVolume.text)
   for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Volume'}):
      circulatingSupplys.append(circulatingSupply.text)
 
pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys})
print(pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys}))
