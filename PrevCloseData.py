from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WebDriverWait
import pandas as pd
import sqlalchemy
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains


url2 = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/theoritical-market-watch-today?locale=en'
driver = webdriver.Chrome(service=Service('/Users/malsaif/Documents/chromedriver-mac-x64/chromedriver'))
driver.get(url2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="theoreticalTableId"]/tbody')))
table = driver.find_element(By.XPATH,'//*[@id="theoreticalTableId"]/tbody')
driver.execute_script("arguments[0].click();", table)
driver.execute_script("arguments[3000].scrollIntoView();", table)

# bottom_element = driver.find_element(By.XPATH, '//*[@id="theoreticalTableId"]/tbody/tr[249]/td[3]')
# bottom_element.location_once_scrolled_into_view 
# PrevCloseList = driver.find_elements(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div/div/section/section[2]/div/div/div/table/tbody/tr/td[3]')

PrevClose = driver.find_elements(By.XPATH, '//*[@id="theoreticalTableId"]/tbody/tr/td[3]')


   



 # //*[@id="theoreticalTableId"]/tbody/tr/td[3]/
df = pd.DataFrame(columns =["PrevClose"])
for i in range(len(PrevClose)):
   df = df._append( {"PrevClose": PrevClose[i].text}, ignore_index = True)

df.to_json(orient='index', path_or_buf="PrevCloseExtract.json")
