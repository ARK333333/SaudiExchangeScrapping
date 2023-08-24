from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sqlalchemy

# URL source
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/indices-performance?locale=en'

# initate WebDriver and get the targeted website URl
driver = webdriver.Chrome(service=Service('/Users/malsaif/Documents/chromedriver-mac-x64/chromedriver'))
driver.get(url)
# Web scraping addresses + segments operations for parts needed
Value = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[2]/div/section/section/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[2]')
ChangeValue = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[2]/div/section/section/div/div[2]/div[1]/div/div[2]').get_attribute("innerHTML").split("<i></i>")[1].split('(')[0]
ChangeRatio = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[2]/div/section/section/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[3]')
TradeVolume = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[7]/strong')
TradesVolume = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[5]/strong')
Open = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[2]/strong')
Close = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[1]/strong')
high = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[3]/strong').get_attribute("innerHTML").split("-")[0]
low = driver.find_element(By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[3]/div/section/section/section[2]/section[1]/div[1]/ul/li[3]/strong').get_attribute("innerHTML").split("-")[1]
PTE = 0 # driver.find_elements(By.XPATH, '')
BVM = 0  # driver.find_elements(By.XPATH, '')

# Transferring data into a dataframe using Panda
df = pd.DataFrame(columns =["Value", "ChangeValue", "ChangeRatio", "TradeVolume", "TradesVolume", "PTE", "BVM", "Open", "Close"])
df = df._append({'Value': Value.text, 'ChangeValue':ChangeValue, 'ChangeRatio': ChangeRatio.text, 'TradeVolume':TradeVolume.text, 'TradesVolume': TradesVolume.text, 'Open': Open.text, 'Close': Close.text, 'High': high, 'Low': low }, ignore_index = True)

# Exporting the dataframe into an index format JSON file named "TasiMarketExtract".
df.to_json(orient='index', path_or_buf="TasiMarketExtract.json")
