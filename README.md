# DiffusionFiji

This is for a task for the Diffusion of Conservation Strategy group I work with (mainly based at Graham Institute, Imperial College London). 

coordinate_finder.py is used to find lat long coordinates of a government-registered list of lodgings in Fiji. 
It does so using Google Geocoding API, which requires you to have a personal API key, which is free from registering with Google Maps API platform. The REQUESTS package in Python pulls the information from the API, as long as the parameters are specified correctly (refer to Google developer documentation(https://developers.google.com/maps/documentation/geocoding/overview)). 

GoogleMap_Webscraping.py file uses SELENIUM (https://www.selenium.dev/selenium/docs/api/py/api.html). It requires a browser driver which you can download for free for your preferred browser. It collects unique establishment names from any Google Map searches.

Fiji_hotel_compare.py is used to see how many hotels from the Fiji gov website matched with the results generated from Google Maps.


## Quick Start
To find coordinates for a list of locations/businesses/etc, use coordinate_finder.py.
Replace capitalised strings in the code before running.
The country code restrict finding to a certain region; use the two letter code (e.g. Japan = jp)

To find a list of business names for a certain type of establishment (e.g. hotels, restaurants) in a certain region, use GoogleMap_Webscraping.py.
Replace capitalised strings in the code before running (the path to your chrome driver, the URL, and the element class*)\
*element class can be found by right-clicking the website for 'inspection', and again right-clicking the element to be collected; the default is set to collect the names of the businesses.

To compare and contrast two lists of business names (e.g. one from government website, the other from Google webscraping), use Fiji_hotel_compare.py.
Simply read in both files.
The coordinates decimal places can be changed (default is 4) to get more matching, however matches can be less accurate.

## Programming Environment
Spyder 4.0.1 in Anaconda 1.9.12

## Dependencies
Google Maps API key (https://cloud.google.com/maps-platform/maps) \
requests (https://pypi.org/project/requests/) \
Chrome_driver.exe (https://chromedriver.chromium.org/downloads)\
selenium (https://www.selenium.dev/selenium/docs/api/py/api.html)\
pandas (https://pandas.pydata.org/)\
numpy (https://numpy.org/)\


