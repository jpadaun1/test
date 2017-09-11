#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:51:15 2017
@author: datascience2
"""


#Important packages needed for my project
import requests
import json
import pandas as pd

"""
import urllib2
import matplotlib.pyplot as plt
import bs4 from BeautifulSoup
import numpy as np
import pandas as pd
import json
import pymongo
from pandas import DataFrame

Google's url for extracting travel times between orgin and destination
url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&key="+api
       
"""

#Jonah Google API key for journey time project
api = "AIzaSyB2mh48lvhGwGs2Ro1lPz7GzvwFePqRCv0"

#***ENGLAND***

#Top 10 Major Cities England
orig_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
dest_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]

#Creates an empty combined list of lists used for appending data collected using Google api key and url 
combined_list_eng=[]
list_labels_eng = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']
    
#Loop for top 10 cities in England
for city_pair_eng in city_pairs_eng:
    url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_eng[0]+"&destinations="+city_pair_eng[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
    r = requests.get(url)
    json_data = r.json()
    data = json.loads(r.text)
    origin = city_pair_eng[0]
    destination = city_pair_eng[1] 
    metres_distance = data['rows'][0]['elements'][0]['distance']['value']
    secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
    secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    country = 'eng' 
    list_cols_eng = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
    combined_list_eng.append(list_cols_eng)

#Pandas DataFrame for top 10 cities in England 
pd_eng=pd.DataFrame(combined_list_eng,columns=list_labels_eng)
print(pd_eng)
pd_eng.to_csv('pd_eng.csv', index=True, header=True, sep=',')


#***FRANCE***

#Top 10 Major Cities in France
orig_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
dest_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
city_pairs_fra=[[i,j] for i in orig_city_fra for j in dest_city_fra if i!=j]

combined_list_fra = []
list_labels_fra = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']
    
#Loop for top 10 cities in France
for city_pair_fra in city_pairs_fra:
    url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_fra[0]+"&destinations="+city_pair_fra[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
    r = requests.get(url)
    json_data = r.json()
    data = json.loads(r.text)
    origin = city_pair_fra[0]
    destination = city_pair_fra[1] 
    metres_distance = data['rows'][0]['elements'][0]['distance']['value']
    secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
    secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    country = 'fra' 
    list_cols_fra = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
    combined_list_fra.append(list_cols_fra)

#Pandas DataFrame for top 10 cities in France 
pd_fra=pd.DataFrame(combined_list_fra,columns=list_labels_fra)
print(pd_fra)
pd_fra.to_csv('pd_fra.csv', index=True, header=True, sep=',')

#appends dataframes
#pd_eng.append(pd_fra)

#Top 10 Major Cities in Germany
#orig_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"] ]
#dest_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"]

#Top 10 Major Cities in Italy 
#orig_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]
#dest_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]   
 
#Top Four Major Cities in Spain
#orig_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]   ]
#dest_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]


