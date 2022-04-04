from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from passenger import passenger as ps
import json
import time
import re
import random
import string
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

output_file = sys.argv[1] if len(sys.argv) > 1 else "southwest_headers.json"

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

seleniumwire_options = {"request_storage": "memory"}

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.scopes = ["page\/check-in"]

driver.get("https://mobile.southwest.com/check-in")
# confirmation_number = "4NKTFU"
# first_name = "Julia"
# last_name = "Siqueira e Silva"



element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "recordLocator")))
element.send_keys(confirmation_number)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(last_name)

element.submit()

time.sleep(10)
southwest_headers = {"content": "json"}
headers = driver.requests[0].headers

for key in headers:
    if re.match("x-api-key|x-user-experience-id|x-channel-id|^[\w-]+?-\w$", key, re.I):
        southwest_headers[key] = headers[key]

with open(output_file, "w") as json_file:
    json.dump(southwest_headers, json_file)

driver.quit()

