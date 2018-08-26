# -*- coding: utf-8 -*-
"""
Daily Update of São Carlos Temperature
using WebScrape
BE SURE TO READ LINE 39
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
from matplotlib import pyplot as plt
import datetime

my_url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/549/saocarlos-sp"

# Opening up connecion, downloading the page itself
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# Grabs minimum and maximum temperatures and write them into csv file
temperature = page_soup.findAll("p", {"class": "left left10 top5 bold font22 txt-black"})
max_temp = temperature[0].text
max_temp = max_temp.replace("°", "")
min_temp = temperature[1].text
min_temp = min_temp.replace("°", "")
# Grabs time and date
time_date_temp = datetime.datetime.now()
time_date = time_date_temp.ctime()

# Setting up external file to receive data
filename = "temperature_saocarlos.csv"
f = open(filename,"a")


# USE THE LINES BELOW (41 AND 42) ON FIRST RUN ONLY!
# =============================================================================
# headers = "maximum,minimum,date\n" 
# f.write(headers)
# =============================================================================

#print("Maximum: " + max_temp)
#print("Minimum: " + min_temp)
#print("Date: " + time_date)
f.write(max_temp + "," + min_temp + "," + time_date + "\n")
f.close()


# Plotting data
data = pd.read_csv("temperature_saocarlos.csv")
temp_max = data.maximum
temp_min = data.minimum
date_time = data.date
comp = len(temp_max)
xaxis = list(range(1, comp+1))
figure0 = plt.figure()
plt.figure(figsize=(30,30))

my_xticks = []
for dt in date_time:
    my_xticks.append(dt)
    
plt.xticks(xaxis, my_xticks, rotation=45)

plt.rcParams.update({'font.size': 22})
plt.title("São Carlos Temperatures",fontsize=40)
plt.plot(xaxis,temp_max, marker='o', linestyle='-', color='b', label='Square')
plt.plot(xaxis,temp_min, marker='o', linestyle='-', color='r', label='Circle')
plt.xlabel("Day",fontsize=40)
plt.ylabel("Temperatures (°C)",fontsize=40)
plt.legend(['Maximum', 'Minimum'])
plt.grid(True)
plt.savefig('SancaTemperatures.png')
plt.close(figure0)
