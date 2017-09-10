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
orig_city_eng = ["london,uk", "manchester, uk"]
dest_city_eng = ["portsmouth, uk", "liverpool, uk"]
city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]


api = "AIzaSyB2mh48lvhGwGs2Ro1lPz7GzvwFePqRCv0"

#empty_dict = {}

#Loop for top 10 cities in England
for city_pair_eng in city_pairs_eng:
    url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_eng[0]+"&destinations="+city_pair_eng[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
    r = requests.get(url)
    #json_data = r.json()
    data = json.loads(r.text)
    origin = city_pair_eng[0]
    destination = city_pair_eng[1] 
    metres_distance = data['rows'][0]['elements'][0]['distance']['value']
    secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
    secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    country = 'uk' 
    #empty_dict[origin+'-'+destination] = [metres_distance, secs_travel_time, secs_travel_time_traffic, country]
    #list_labels = ['origin', 'destination', 'metres_distance', 'secs_travel_time', 'secs_travel_time_traffic', 'country']
    #list_cols = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
    data_dict ={ 'orig' : [origin],
           'dest' : [destination],
           'dist_m' : [data['rows'][0]['elements'][0]['distance']['value']],
           'secs' : [data['rows'][0]['elements'][0]['duration']['value']],
           'secs_traffic' : [data['rows'][0]['elements'][0]['duration_in_traffic']['value']],
           'country' : [country] }
    #print(data_dict)
    # Create an example dataframe

    uk_city_pairs = pd.DataFrame(data_dict)
    print(uk_city_pairs)

#puts data into csv file
uk_city_pairs.to_csv('example.csv', index=True, header=True, sep=',')

    #zipped = list(zip(list_labels, list_cols)) 
   # uk_city_pairs = pd.DataFrame(dict)
    #uk_city_pairs_transpose = uk_city_pairs.T
    #uk_city_pairs_transpose.columns = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']
    #print(uk_city_pairs_transpose)

#uk_city_pairs = uk_city_pairs.T
#uk_city_pairs.to_csv('example.csv', index=False, header=False, sep=',')


   
    
   # dict_uk = {
    #    "origin" : [city_pair_eng[0]],
     #   "destination" : [city_pair_eng[1]],
      #  "metres_distance" : [data['rows'][0]['elements'][0]['distance']['value']],
       # "secs_travel_time" : [ data['rows'][0]['elements'][0]['duration']['value']],
        #"secs_travel_time_traffic" : [data['rows'][0]['elements'][0]['duration_in_traffic']['value']],
        #"country" : ['uk'] }
    
    #Creates Pandas DataFrame for UK city pairs 
#    uk_city_pairs = pd.DataFrame(dict_uk)
 #   print(uk_city_pairs)



#Restore json data into original response format from Google url   
#json.dumps(data)
    
""" 
From my original loop but no longer needed
 
    #print('origin', city_pair_eng[0])
    #print ('destiniation',city_pair_eng[1])
    #print ('(country: uk)')
    #print('metres_distance', data['rows'][0]['elements'][0]['distance']['value'])
    #print('secs_travel_time', data['rows'][0]['elements'][0]['duration']['value'])
    #print('secs_travel_time_traffic', data['rows'][0]['elements'][0]['duration_in_traffic']['value'])
    #print ('country_uk')
    
    #print(json_data)
"""

#Creates England city pairs pandas data frame
#df = DataFrame(data)
#print(df)
#dict_uk = {
  #      "origin" : [city_pair_eng[0]],
   #     "destination" : [city_pair_eng[1]],
    #    "'metres_distance'" : [data['rows'][0]['elements'][0]['distance']['value']],
     #   "secs_travel_time" : [ data['rows'][0]['elements'][0]['duration']['value']],
      #  "secs_travel_time_traffic" : [data['rows'][0]['elements'][0]['duration_in_traffic']['value']],
       # "country" : ['uk'] }

#uk_city_pairs = pd.DataFrame(dict_uk)
#print(uk_city_pairs)

#In [2]: dict = {
 #"country":["Brazil", "Russia", "India", "China", "South Africa"],
# "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
 #"area":[8.516, 17.10, 3.286, 9.597, 1.221]
 #"population":[200.4, 143.5, 1252, 1357, 52.98] }
#keys (column labels) values (data, column by column)
#In [3]: import pandas as pd
#In [4]: brics = pd.DataFrame(dict)


#Top 10 Major Cities in France
#orig_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
#dest_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]

#Top 10 Major Cities in Germany
#orig_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"] ]
#dest_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"]

#Top 10 Major Cities in Italy 
#orig_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]
#dest_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]   
 
#Top Four Major Cities in Spain
#orig_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]   ]
#dest_city_spa = ["madrid, spain, "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]


#Top Four Major Cities Netherlands
#orig_city_ned = [am]


"""
Me trying to convert a dictionary into a pandas DataFrame!
json_dict = {
        "city":[],
        "distance":[],
        "duration":[],
        "duration_in_traffic":[]}
city_pairs_r_data = pd.DataFrame(json_dict)
data = r.json
lat,lng,el = [],[],[]
for result in data['results']:
    lat.append(result[u'location'][u'lat'])
    lng.append(result[u'location'][u'lng'])
    el.append(result[u'elevation'])
city_pairs_ex = pd.DataFrame([lat,lng,el]).T
"""

"""
Code I might use later 
#print r.status_code
#print r
#print type(r)
#print r.json
"""