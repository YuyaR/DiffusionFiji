#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Mar 30 12:43:39 2021

@author: yuyara
"""


import requests as rq
import pandas as pd

#function that returns lat long for most business names/formatted address
#require personal google API key
#strings that require user input is CAPITALISED

def locate(location,country_code): #country_code, a 2-letter unique code
    parameter = {"address":location,"key":"YOUR_API_KEY", "components":"country:"+country_code}
    result = rq.get("https://maps.googleapis.com/maps/api/geocode/json", params=parameter)
    resultText = eval(result.text)
    find = resultText["results"][0]["geometry"]["location"]
    return(find["lat"],find["lng"])


hotel_list = pd.read_csv("FILE_WITH_HOTEL_NAMES.csv") 


latitude = []
longitude = []
fail_list = []
for hotel in hotel_list["Names_Of_Premises"]:
    try:
        coordinates = locate(hotel,"fj")
        latitude.append(coordinates[0])
        longitude.append(coordinates[1])
    except NameError:
        print(hotel+" can't be found :(")
        fail_list.append(hotel)
        latitude.append("NA")
        longitude.append("NA")
    except IndexError:
        print(hotel+" index??")
        fail_list.append(hotel)
        latitude.append("NA")
        longitude.append("NA")
    #indexing error appeared rarely.
    
hotel_list["latitude"] = latitude
hotel_list["longitude"] = longitude

hotel_list.to_csv(r'LOCATION/PATH/FILE_NAME.csv', index=False, header=True)

