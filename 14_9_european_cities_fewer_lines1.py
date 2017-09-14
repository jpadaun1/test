#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:58:38 2017

@author: datascience2
"""


#Important packages needed for my project
import requests
import json
import pandas as pd

"""
Some other potential packages to use 

import matplotlib.pyplot as plt
import bs4 from BeautifulSoup?
import numpy as np
import pymongo?

Google's url for extracting travel times between orgin and destination
url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&key="+api
       
"""

#Jonah Google API key for international journey time benchmarking project
api = "AIzaSyB2mh48lvhGwGs2Ro1lPz7GzvwFePqRCv0"

#The following lines of code defines the cities used for each of the 5 countries 

#Top 10 most polulated cities England
orig_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
dest_city_eng = ["london, uk", "birmingham, uk", "manchester, uk", "liverpool, uk", "newcastle, uk", "nottingham, uk", "sheffield, uk", "leeds, uk", "bristol, uk", "middlesbrough, uk"]
city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]

#Top 10 most populated cities in France
orig_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
dest_city_fra = ["paris, france", "marseille, france", "lyon, france", "toulouse, france", "nice, france", "nantes, france", "strasbourg, france", "montpellier, france", "bordeaux, france", "lille, france"]
city_pairs_fra=[[i,j] for i in orig_city_fra for j in dest_city_fra if i!=j]

#Top 10 most populated cities in Germany
orig_city_ger = ["berlin, germany","hamburg, germany",  "münchen, germany", "köln, germany", "frankfurt, germany", "essen, germany", "dortmund, germany", "stuttgart, germany", "düsseldorf, germany", "bremen, germany"] 
dest_city_ger = ["berlin, germany","hamburg, germany",  "münchen, germany", "köln, germany", "frankfurt, germany", "essen, germany", "dortmund, germany", "stuttgart, germany", "düsseldorf, germany", "bremen, germany"] 
city_pairs_ger=[[i,j] for i in orig_city_ger for j in dest_city_ger if i!=j]

#Top 10 most populated cities in Italy
orig_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]
dest_city_ita = ["roma, italy", "milano, italy", "napoli, italy", "torino, italy", "palermo, italy", "genova, italy", "bologna, italy", "florence, italy", "cantania, italy", "bari, italy"]   
city_pairs_ita=[[i,j] for i in orig_city_ita for j in dest_city_ita if i!=j]

#Top 10 most populated cities in Spain
orig_city_spa = ["madrid, spain", "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]   
dest_city_spa = ["madrid, spain", "barcelona, spain", "valencia, spain", "seville, spain", "zaragoza, spain", "málaga, spain", "muria, spain", "palma, spain", "Las Palmas de Gran Canaria, spain", "bilbao, spain"]
city_pairs_spa=[[i,j] for i in orig_city_spa for j in dest_city_spa if i!=j]

#The following lines of code creates an empty list for each country to store Google JSON and label the 6 key columns accordingly  

#Creates an empty combined list of lists used for appending data collected using Google api key and url 

#England
combined_list_eng=[]
list_labels_eng = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']

#France
combined_list_fra = []
list_labels_fra = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']

#Italy
combined_list_ita = []
list_labels_ita = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']

#Germany
combined_list_ger = []
list_labels_ger = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']

#Spain
combined_list_spa = []
list_labels_spa = ['orig', 'dest', 'dist_m', 'secs', 'secs_traf', 'country']

 
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
 
#Loop for top 10 cities in Germany
    for city_pair_ger in city_pairs_ger:
        url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_ger[0]+"&destinations="+city_pair_ger[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
        r = requests.get(url)
        json_data = r.json()
        data = json.loads(r.text)
        origin = city_pair_ger[0]
        destination = city_pair_ger[1] 
        metres_distance = data['rows'][0]['elements'][0]['distance']['value']
        secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
        secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
        country = 'ger' 
        list_cols_ger = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
        combined_list_ger.append(list_cols_ger)

#Loop for top 10 cities in Italy
    for city_pair_ita in city_pairs_ita:
        url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_ita[0]+"&destinations="+city_pair_ita[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
        r = requests.get(url)
        json_data = r.json()
        data = json.loads(r.text)
        origin = city_pair_ita[0]
        destination = city_pair_ita[1] 
        metres_distance = data['rows'][0]['elements'][0]['distance']['value']
        secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
        secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
        country = 'ita' 
        list_cols_ita = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
        combined_list_ita.append(list_cols_ita)
    
#Loop for top 10 cities in Spain
    for city_pair_spa in city_pairs_spa:
        url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_spa[0]+"&destinations="+city_pair_spa[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
        r = requests.get(url)
        json_data = r.json()
        data = json.loads(r.text)
        origin = city_pair_spa[0]
        destination = city_pair_spa[1] 
        metres_distance = data['rows'][0]['elements'][0]['distance']['value']
        secs_travel_time =  data['rows'][0]['elements'][0]['duration']['value']
        secs_travel_time_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
        country = 'spa' 
        list_cols_spa = [origin, destination, metres_distance, secs_travel_time,secs_travel_time_traffic, country]
        combined_list_spa.append(list_cols_spa)


#Pandas DataFrame for top 10 cities in England 
pd_eng=pd.DataFrame(combined_list_eng,columns=list_labels_eng)
print(pd_eng)
pd_eng.to_csv('pd_eng.csv', index=True, header=True, sep=',')

#Pandas DataFrame for top 10 cities in France 
pd_fra=pd.DataFrame(combined_list_fra,columns=list_labels_fra)
print(pd_fra)
pd_fra.to_csv('pd_fra.csv', index=True, header=True, sep=',')

#Pandas DataFrame for top 10 cities in Germany 
pd_ger=pd.DataFrame(combined_list_ger,columns=list_labels_ger)
print(pd_ger)
pd_ger.to_csv('pd_ger.csv', index=True, header=True, sep=',')

#Pandas DataFrame for top 10 cities in Italy 
pd_ita=pd.DataFrame(combined_list_ita,columns=list_labels_ita)
print(pd_ita)
pd_ita.to_csv('pd_ita.csv', index=True, header=True, sep=',') 

#Pandas DataFrame for top 10 cities in Spain 
pd_spa=pd.DataFrame(combined_list_spa,columns=list_labels_spa)
print(pd_spa)
pd_spa.to_csv('pd_spa.csv', index=True, header=True, sep=',') 


#appended dataframes for all countries 
master_data = pd_eng.append([pd_fra,pd_ger,pd_ita,pd_spa])
print(master_data)
master_data.to_csv('master_data.csv', index=False, header=True, sep=',')