#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:51:25 2021

@author: yuyara
"""

import pandas as pd

google_hotel = pd.read_csv("PATH/TO/Google_Fijihotel.csv")

unique_google = google_hotel.drop_duplicates(["rounded_latitude", "rounded_longitude"])

#double check the duplicates
print(google_hotel[google_hotel.duplicated(["rounded_latitude", "rounded_longitude"], keep=False)])

final_results = unique_google[['Name of Hotel', 'latitude', 'longitude', 'found on fiji gov website']]

final_results.to_csv("PATH/TO/SAVE/FILE/Google_FijiHotel_final.csv", index=False, header=True)
