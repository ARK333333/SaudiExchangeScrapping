from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sqlalchemy

url2 = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/theoritical-market-watch-today?locale=en'
driver = webdriver.Chrome(service=Service('/Users/malsaif/Documents/chromedriver-mac-x64/chromedriver'))
driver.get(url2)
PrevClose = driver.find_elements(By.XPATH, '//*[@id="theoreticalTableId"]/tbody/tr/td[3]')


df = pd.DataFrame(columns =["PrevClose"])
for i in range(len(PrevClose)):
   df = df._append( {'PrevClose': PrevClose[i].text}, ignore_index = True)
df.to_json(orient='index', path_or_buf="PrevCloseExtract.json")
