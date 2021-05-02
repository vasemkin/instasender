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
import win32clipboard

with open('auth.json') as f:
    auth = json.load(f)

win32clipboard.OpenClipboard()
clipboard_data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(f'sending message: \n{clipboard_data}')

mla_profile_id = auth['profile']

mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id
resp = requests.get(mla_url)

json = resp.json()

opts = options.DesiredCapabilities()
driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})

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
            
            driver.get(link)
            followers_file.write(line + '\n')
            print(line)

            
            def exists(css):
                try:
                    driver.find_element_by_css_selector(css)
                except NoSuchElementException:
                    return False
                return True

            follow_css = '#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button'
            
            if (exists(follow_css)):
                follow_button = driver.find_element_by_css_selector(follow_css)
                if (follow_button.text == 'Follow'):
                    follow_button.click()
                    print('following')
                    dream('long')
                else : 
                    print('already followed')
            else:
                print('follow button not located')
            
            dream('long')

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