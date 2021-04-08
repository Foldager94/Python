from selenium import webdriver
import bs4
import json
import requests
import re
import regex
import datetime

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Webscraper:

    def __init__(self, url):
        self.url = url
        

    
    def search(self, param):
        options = Options()
        options.headless = True
        print("Initialzin webdriver")
        start = datetime.datetime.now()
        browser = webdriver.Firefox(options=options)

        print()
        print("Fetching url")
        browser.get(self.url)
        print("Telling browser to wait 2 sec by deault")
        browser.implicitly_wait(2)
        
        browser.find_elements_by_tag_name('button')[1].click()
        browser.implicitly_wait(2)

        #browser.find_element_by_xpath("//a[@href='/cl/37/Grafikkort?attr_50615361=56611824']").click()
        browser.find_elements_by_class_name('_2Jn2-PLos3')[0].click()
        browser.implicitly_wait(10)
        browser.find_elements_by_class_name('_3kbvwJ4edH')[0].click()
        string_url = browser.current_url
        print(string_url)
        req = requests.get(string_url)
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        #print(soup)
        #print(browser.find_elements_by_partial_link_text("/cl/37/Grafikkort?attr_50615361=56611824"))
        #print(browser.find_elements_by_id('Title'))   
        #button = browser.find_element_by_id('declineButton')
        #button.click()
        mydivs = soup.find_all("div", {"class": "_2Vdwcz_zWR _1bgVr-M90D"})
        #print(mydivs[0])
        #File_object = open(r"gpu_stuff.txt","w")
        #File_object.write(str(mydivs))
        #print( re.findall("^3060", "gpu_stuff.txt") )
        #print("wtf")
        print("####################")
        for card in mydivs:
            print(card.find("div", {"class" : "_3jyYcmGfmy"}).get('title', 'No title found'))
            print('------------------------------')
        
        finish = datetime.datetime.now()
        print(finish - start)
        
        