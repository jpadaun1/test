#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:51:15 2017

@author: datascience2
"""

import requests
import

"""
import urllib2
import bs4 from BeautifulSoup
import numpy as np
import pandas as pd
import json
import pymongo


Google's url for extracting travel times between orgin and destination
url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&key="+api
       

"""

#Top Four Major Cities England
orig_city_eng = ["london,uk", "manchester, uk", "bristol, uk", "leeds, uk", "birmingham, uk", "newcastle, uk", "brighton, uk", "southampton, uk", "liverpool, uk", "portsmouth, uk"]
dest_city_eng = ["portsmouth, uk", "liverpool,uk", "southampton, uk", "brighton, uk", "newcastle, uk", "brimingham, uk", "leeds, uk", "bristol, uk", "manchester, uk", "london,uk" ]
city_pairs_eng=[[i,j] for i in orig_city_eng for j in dest_city_eng if i!=j]


api = "AIzaSyB2mh48lvhGwGs2Ro1lPz7GzvwFePqRCv0"

#Loop for cities in England
for city_pair_eng in city_pairs_eng:
    url =  "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+city_pair_eng[0]+"&destinations="+city_pair_eng[1]+"&departure_time=now&traffic_model=best_guess&key="+api       
    r = requests.get(url)
    #json_data = r.json()
    print('origin',city_pair_eng[0],'destiniation',city_pair_eng[1])
    print(r.text)
    #print(json_data)

'''
me trying to store 

for item in r.text['elements']:
    print item

'''

#Top Four Major Cities in France
#orig_city_fra = ["paris, france", ]
#orig_dest_fra = 

#Top Four Major Cities in Germany
#orig_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"] ]
#dest_city_ger = ["berlin, germany", "munich, germany", "frankfurt, germany", "hamburg, germany", "cologne, germany", "dresden, germany", "leipzig, germany", "heidelberg, germany", "düsseldorf, germany"]
    
#Top Four Major Cities in Spain
#orig_city_spa = ["madrid, spain"]

#Top Four Major Cities in Italy 
#orig_city_ita = ["rome, italy"]

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