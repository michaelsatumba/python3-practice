from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()

#browser.get('https://automatetheboringstuff.com/')
browser.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in')
#/html/body/div/main/div//ul[2]/li[1]/a
#element = browser.find_element("xpath", "//html/body/div/main/div//ul[2]/li[1]/a")
#element.click()

from dotenv import load_dotenv
load_dotenv()


import os
#print(os.environ)
nameInsert = os.getenv("NAME")
passwordInsert = os.getenv("PASSWORD")
#print(nameInsert)


username = browser.find_element("xpath", "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
username.send_keys(nameInsert)

password = browser.find_element("xpath", "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
password.send_keys(passwordInsert)
username.submit()

jobs = browser.find_element("xpath", "/html/body/div[5]/header/div/nav/ul/li[3]/a")
jobs.click()

time.sleep(5)

searchJob =  browser.find_element("xpath","//div/div/input[1]")
#print(searchJob)
searchJob.send_keys("software developer")
searchJob.send_keys(Keys.RETURN)

#jobs-search-box-keyword-id-ember353
#jobs-search-box-keyword-id-ember346
#keyword-typeahead-instance-ember346 > div > input:nth-child(3)
#/html/body/div[5]/header/div/div/div/div[2]/div[3]/div/div/input[1]
