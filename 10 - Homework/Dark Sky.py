#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


##To do: 
#TEMPERATURE is the current temperature
#SUMMARY is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
#TEMP_FEELING is whether it will be hot, warm, cold, or moderate. You will probably use HIGH_TEMP and your own thoughts and feelings to determine this.
#HIGH_TEMP is the high temperature for the day.
#LOW_TEMP is the low temperature for the day.
#RAIN_WARNING is something like "bring your umbrella!" if it is going to rain at some point during the day.


# In[3]:


#https://api.darksky.net/forecast/45c936bb848da3589b123bf7083f5109/37.8267,-122.4233


# In[4]:


response = requests.get('https://api.darksky.net/forecast/45c936bb848da3589b123bf7083f5109/37.8267,-122.4233')
data = response.json()
print(data)


# In[5]:


response = requests.get('https://api.darksky.net/forecast/45c936bb848da3589b123bf7083f5109/37.8267,-122.4233')
nyc = response.json()
print(nyc)


# In[6]:


nyc.keys()


# In[7]:


current_temperature = nyc['currently']['temperature']
current_temperature


# In[8]:


summary = nyc['currently']['summary']
summary


# In[9]:


temp_feeling = nyc['currently']['temperature']

if temp_feeling > 25:
    print("hot")
elif temp_feeling < 15:
    print("cold")
else:
    print("warm")


# In[10]:


daily = nyc['daily']['data'][0]
    
print(daily['temperatureMax'])


# In[11]:


daily = nyc['daily']['data'][0]
    
print(daily['temperatureMin'])


# In[12]:


print(daily['precipProbability'])


# In[13]:


rain_warning = daily['precipProbability']

if rain_warning > 0.5:
    sentence = "Right now it is "+str(current_temperature)+" degrees out and "+summary+". Today will be "+str(temp_feeling)+" with a high of "+str(daily['temperatureMax'])+" and a low of "+str(daily['temperatureMin'])+" degrees. It's going to rain. Make shure to leave home with an umbrella!"

else:
    sentence = "Right now it is "+str(current_temperature)+" degrees out and "+summary+". Today will be "+str(temp_feeling)+" with a high of "+str(daily['temperatureMax'])+" and a low of "+str(daily['temperatureMin'])+" degrees. It's not going to rain. You will not need an umbrella (hopefully)!"
    
print(sentence)


# In[14]:


import datetime
right_now = datetime.datetime.now()
right_now

response = requests.post(
        "https://api.mailgun.net/v3/sandbox5ec0ddffbdba4001b8214f98622fe1d0.mailgun.org/messages",
        auth=("api", "6fdb842f47e65d63dd61f10b38545e63-2b778fc3-8157d877"),
        data={"from": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "to": "giovanacfleck@gmail.com",
              "subject": "8AM Weather forecast: "+ str(right_now.strftime("%Y-%m-%d")),
              "text": sentence})


# In[ ]:




