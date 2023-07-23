from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sqlalchemy
# URL source
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch'

# initate WebDriver and get the targeted website URl
driver = webdriver.Chrome(service=Service('/Users/saif/Downloads/chromedriver_mac64/chromedriver'))
driver.get(url)

#Scrapping Parts, different desired parts of the table. They are located using their XPATHs
TickersID = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[1]')
Prices = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[2]')
TradeChangeValue =  driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[4]')
TradeChangePercentage =  driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[5]')
NumberOfTrades =  driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[6]')
VolumesTraded = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[7]')
Open = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[8]')
High = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[9]')
Low = driver.find_elements(By.XPATH, '//div[@class="dataTables_scrollBody"]//tbody/tr//td[10]')

# Transferring data into a dataframe using Panda
df = pd.DataFrame(columns =["TickersID", "Price", "Trade Change Value", "Trade Change Percentage", "Number of Trades","Volume Traded","Open","High","Low"])
for i in range(len(TickersID)):
    df = df._append({'TickersID': TickersID[i].text, 'Price':Prices[i].text, 'Trade Change Value': TradeChangeValue[i].text, 'Trade Change Percentage': TradeChangePercentage[i].text, 'Number of Trades': NumberOfTrades[i].text, 'Volume Traded': VolumesTraded[i].text,'Open': Open[i].text, 'High': High[i].text, 'Low': Low[i].text}, ignore_index = True)

# Exporting the dataframe into an index format JSON file named "TasiExtract".
df.to_json(orient='index', path_or_buf="TasiExtract.json")