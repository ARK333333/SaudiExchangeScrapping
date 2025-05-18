from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

# URL source
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/reports-publications/historical-reports/'

driver = webdriver.Firefox(options=Options())

driver.get(url)
dropdown = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[1]/div/div/button')))
driver.execute_script("arguments[0].click();", dropdown)

market = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="bs-select-1-1"]')))
market.click()

#sectors scrape
dropdown_sectors = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[2]/div/div/button')))
driver.execute_script("arguments[0].click();", dropdown_sectors)

# Wait for dropdown to be fully visible
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[2]/div/div/div/div[2]/ul')))

# Get all sector items directly with a single call
sector_items = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.XPATH, '//html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[2]/div/div/div/div[2]/ul/li')))

# loop through the sectors
for i in range(len(sector_items)):
    # Click on the sector
    print(f"Attempting to click: {sector_items[i].text}")
    ActionChains(driver).move_to_element(sector_items[i]).click().perform()
    driver.execute_script("arguments[0].click();", dropdown_sectors)

# Print the sector you want to click

# Wait explicitly for this specific item to be clickable
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{sector_items[3].text}')]")))

# Click using the action chain for more reliable clicking


# Alternative clicking approach (if needed)
# driver.execute_script("arguments[0].scrollIntoView(true);", sector_items[3])
# driver.execute_script("arguments[0].click();", sector_items[3])

# for sector in sectors_list:
#     print(sector.text)

#     # Click on the sector
#     driver.execute_script("arguments[0].click();", sector)
#     print(sector.text, "clicked")
#     # Wait for the entities to load
#     print(entities_scrape())
    
#     #go back to dropmenu
#     driver.execute_script("arguments[0].click();", dropdown_sectors)



    # sector_element = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.XPATH, f'//li[contains(text(), "{sector}")]')))
    # driver.execute_script("arguments[0].click();", sector_element)
    # # entities = entities_scrape()
    # # for entity in entities:
    # #     print(entity.text)
    # driver.execute_script("arguments[0].click();", dropdown_sectors)

# Transferring data into a dataframe using Panda
# df = pd.DataFrame(columns =["Value", "ChangeValue", "ChangeRatio", "TradeVolume", "TradesVolume", "PTE", "BVM", "Open", "Close"])
# df = df._append({'Value': Value.text, 'ChangeValue':ChangeValue, 'ChangeRatio': ChangeRatio.text, 'TradeVolume':TradeVolume.text, 'TradesVolume': TradesVolume.text, 'Open': Open.text, 'Close': Close.text, 'High': high, 'Low': low }, ignore_index = True)

# # Exporting the dataframe into an index format JSON file named "TasiMarketExtract".
# df.to_json(orient='index', path_or_buf="TasiMarketExtract.json")
