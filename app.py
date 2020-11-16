from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException       
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json
import random

with open('auth.json') as f:
    auth = json.load(f)

#TODO replace with existing profile ID. Define the ID of the browser profile, where the code will be executed.
mla_profile_id = auth['profile']

mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id

"""
Send GET request to start the browser profile by profileId. Returns response in the following format: '{"status":"OK","value":"http://127.0.0.1:XXXXX"}', where XXXXX is the localhost port on which browser profile is launched. Please make sure that you have Multilogin listening port set to 35000. Otherwise please change the port value in the url string
"""
resp = requests.get(mla_url)

json = resp.json()

#Define DesiredCapabilities
opts = options.DesiredCapabilities()

#Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})

#Perform automation

def dummy_send(element, word):    
    for c in word:
        delay = random.uniform(0.03, 0.2)
        element.send_keys(c)
        time.sleep(delay)

def dream(length):
    out = 0
    if length == 'long':
        out = random.uniform(2.1, 4.8) 
    else:
        out = random.uniform(0.5, 1.8)
    time.sleep(out)

def login():

    driver.get("https://instagram.com/accounts/login")

    time.sleep(3)
    login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
    password = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
    submit = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')

    dummy_send(login, auth['login'])
    dream('short')
    dummy_send(password, auth['pass'])
    dream('short')
    submit.click()

def spam():


    followers_file = open('spammed_followers.txt', 'a')

    with open('followers.txt') as f:
        for line in f:
            link = 'https://instagram.com/' + line + '/'
            #link = 'https://www.instagram.com/reyokiko/'
            driver.get(link)
            followers_file.write(line + '\n')
            print(line)
            dream('long')

            def exists(css):
                try:
                    driver.find_element_by_css_selector(css)
                except NoSuchElementException:
                    return False
                return True
            

            open_dialog_css = '#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div._862NM > div > button'

            if (exists(open_dialog_css)):
                open_dialog_css = driver.find_element_by_css_selector(open_dialog_css)
                open_dialog_css.click()
                print('dialog opened')
                dream('long')

                textarea = driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
                
                textarea.send_keys(Keys.CONTROL, 'v')

                print('paste completed')
                dream('short')

                send_button = driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button')
                send_button.click()
                dream('long')

            else:
                print('well Shit')


spam()


time.sleep(60)