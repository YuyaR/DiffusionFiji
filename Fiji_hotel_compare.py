#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:33:24 2021

@author: yuyara
"""
import pandas as pd
import requests as rq

Google_results = []
with open("PATH/TO/Google_results.txt") as file:
    for line in file:
        Google_results.append(line)


hotel_list = pd.read_csv("PATH/TO/hotel_list2.csv")

#using geocoding to find coordinates for Google_results



def locate(location,country):
    parameter = {"address": location, "key": "PERSONAL_API_KEY", "components": "country:"+country}
    result = rq.get("https://maps.googleapis.com/maps/api/geocode/json", params=parameter)
    resultText = result.text.replace("true", "True")
    resultText = resultText.replace("false", "False")
    resultText = eval(resultText)
    find = resultText["results"][0]["geometry"]["location"]
    return(find["lat"],find["lng"])

latitude = []
longitude = []

for g in Google_results:
    coordinates = locate(g, "fj")
    latitude.append(coordinates[0])
    longitude.append(coordinates[1])

#the coordinates for both lists of results are rounded to 4 decimals for consistency
Google_latitude = [round(x,4) for x in latitude] 
Google_longitude = [round(y,4) for y in longitude] 

Gov_latitude = [round(z,4) for z in hotel_list["latitude"]]
Gov_longitude = [round(p,4) for p in hotel_list["longitude"]]

comp_list = []
for k in range(0,237):
    if (Google_latitude[k] in Gov_latitude) and (Google_longitude[k] in Gov_longitude):
        comp_list.append("Yes")
    else:
        comp_list.append("No")

#with 4 decimal: 81 yes
#3 decimals: 90 yes
#2 decimals: 154 yes
#with 2 decimals it is a mess :( 
#3 decimals: mostly accurate besides 4-5 places with identical lat long
#4 decimals: all matched up. can see how different some names are across websites though.


Google_Fijihotel = {"Name of Hotel": Google_results, "latitude": latitude, "longitude": longitude, "found on fiji gov website": comp_list}
Google_Fijihotel = pd.DataFrame(Google_Fijihotel)

#the matching hotels are merged so the names can be manually confirmed to be matching
Google_Fijihotel["rounded_latitude"] = Google_latitude
Google_Fijihotel["rounded_longitude"] = Google_longitude

hotel_list["rounded_latitude"] = Gov_latitude
hotel_list["rounded_longitude"] = Gov_longitude

Both_hotel = pd.merge(Google_Fijihotel[["Name of Hotel", "found on fiji gov website", "rounded_latitude", "rounded_longitude"]], hotel_list[["Names  Of  Premises", "rounded_latitude", "rounded_longitude"]], how="inner", left_on=["rounded_latitude","rounded_longitude"], right_on=["rounded_latitude","rounded_longitude"])


Google_Fijihotel.to_csv(r'~/Desktop/python/Fiji/Google_Fijihotel.csv', index=False, header=True)

