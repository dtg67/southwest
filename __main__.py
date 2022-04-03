import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import csv

# PATH = "~/Downloads/chromedriver"
# driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.southwest.com/air/check-in/index.html")

time.sleep(2)

input_confirm = driver.find_element("confirmationNumber")
input_fname = driver.find_element('passengerFirstName')
input_lname = driver.find_element('passengerLastName')

input_confirm.send_keys('4NKTFU')
time.sleep(2)
input_fname.send_keys('Julia')
time.sleep(2)
input_lname.send_keys('Chow')
time.sleep(2)

checkin_btn = driver.find_element('form-mixin--submit-button')
print('pppp')
checkin_btn.click()
time.sleep(20)
print('yyyyy')
