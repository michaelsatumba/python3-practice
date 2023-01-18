from selenium import webdriver
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
#print(nameInsert)


username = browser.find_element("xpath", "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
username.send_keys(nameInsert)

password = browser.find_element("xpath", "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
password.send_keys('path')
#username.submit()

jobs = browser.find_element("xpath", "/html/body/div[5]/header/div/nav/ul/li[3]/a")
jobs.click()


