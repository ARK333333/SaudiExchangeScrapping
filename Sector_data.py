from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sqlalchemy
# URL source
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/marketsummary?locale=en'

# initate WebDriver and get the targeted website URL
driver = webdriver.Chrome(service=Service('/Users/malsaif/Documents/chromedriver-mac-x64/chromedriver'))
driver.get(url)

#Scrapping Parts, different desired parts of the table. They are located using their XPATHs
SectorColumn =  driver.find_elements(By.XPATH,'//*[@id="layoutContainers"]/div[3]/div[3]/div/section/section/div[2]/table/tbody/tr/td')
SectorID = driver.find_elements(By.XPATH, '//*[@id="layoutContainers"]/div[3]/div[3]/div/section/section/div[2]/table/tbody/tr/td/div[1]')
SectorPoints = driver.find_elements(By.XPATH, '//*[@id="layoutContainers"]/div[3]/div[3]/div/section/section/div[2]/table/tbody/tr/td/div[2]')
SectorRatio = driver.find_elements(By.XPATH, '//*[@id="layoutContainers"]/div[3]/div[3]/div/section/section/div[2]/table/tbody/tr/td/div[3]')

# Transferring data into a dataframe using Panda
df = pd.DataFrame(columns =["SectorID", 'SectorPoints','SectorRatio'])
for i in range(len(SectorColumn)):
    df = df._append( {'SectorID': SectorID[i].text, 'SectorPoints':SectorPoints[i].text, 'SectorRatio': SectorRatio[i].text}, ignore_index = True)

# Exporting the dataframe into an index format JSON file named "TasiSectorExtract".
df.to_json(orient='index', path_or_buf="TasiSectorExtract.json")
 

