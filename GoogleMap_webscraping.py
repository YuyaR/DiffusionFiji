#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:47:06 2021

@author: yuyara
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:05:06 2021

@author: yuyara
"""

#strings that require user input is CAPITALISED

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import time

#Browser initiation process; require chrome driver
#Note about time.sleep: depending on your wifi speed etc,
#it might take longer or slower to load some components
#so modify the time if needed
options = Options()
options.headless = True #Specify True for the browser to open, False to keep it running in the background

driver_path = "/PATH/TO/CHROMEDRIVER"
driver = webdriver.Chrome(options=options, executable_path=driver_path)

url = "URL_OF_GOOGLE_MAP_TEXT_SEARCH " #Google Map search the wanted establishment types in certain region using "type"+"in"+"location

driver.get(url)

time.sleep(2)

#click "I agree" botton on the cookie agreement pop-up page in order to proceed
button = driver.find_elements_by_xpath("//*[contains(text(), 'I agree')]")
action = ActionChains(driver)

action.move_to_element(button[0]).click().perform()

time.sleep(3)

#Establishment (e.g. hotel) name extraction
results = []

while True:
    #need to click on first result to load all items on one page
    action = ActionChains(driver)
    action.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
    action.move_by_offset(20,500).click().perform()
    
    time.sleep(1)
    
    class_name = 'rLwmCGCu6mP__title'      
    #find this by right-clicking the browser to inspect the source code, and then 
    #specifically right click on wanted information to 'inspect', which should 
    #show a block of code containing 'class = xxxx'
    
    elements = driver.find_elements_by_class_name(class_name)
    for el in elements:
        results.append(el.text)
        print(el.text)
    
    time.sleep(4)
    #back to results and click next page and repeat
    back_to_result = driver.find_element_by_xpath("//*[contains(text(), 'Back to results')]")
    action.move_to_element(back_to_result).click().perform()
    
    time.sleep(1)
    
    action = ActionChains(driver)
    next_page = driver.find_element_by_id('n7lv7yjyC35__section-pagination-button-next')
    action.move_to_element(next_page).click().perform()
    
    time.sleep(3)

#Due to some overlap in each page, redundant results are collected
Final_results = np.unique(results)

np.savetxt("FILE_NAME.txt", X=Final_results, newline='\n', fmt='%s')
