#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:51:15 2017
@author: datascience2
"""

import requests
import json
import pandas as pd




"""
import urllib2
import bs4 from BeautifulSoup
import numpy as np
import pandas as pd
import json
import pymongo
from pandas import DataFrame

Google's url for extracting travel times between orgin and destination
url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&key="+api
       
"""

#Top 10 Major Cities England
orig_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
dest_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]

api = "AIzaSyB2mh48lvhGwGs2Ro1lPz7GzvwFePqRCv0"

combined_list=[]
list_labels = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']
    
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
    list_cols = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
    combined_list.append(list_cols)

#Pandas DataFrame for top 10 cities in England 
pd_eng=pd.DataFrame(combined_list,columns=list_labels)
print(city_pairs_eng)
pd_eng.to_csv('pd_eng.csv', index=True, header=True, sep=',')


#Top 10 Major Cities in France
#orig_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
#dest_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
#city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]

#Top 10 Major Cities in Germany
#orig_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"] ]
#dest_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"]

#Top 10 Major Cities in Italy 
#orig_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]
#dest_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]   
 
#Top Four Major Cities in Spain
#orig_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]   ]
#dest_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]


