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
import time
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

def entities_scrape():
    time.sleep(2)
    #entities scrape
    dropdown_entities = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[3]/div[1]/div/button')))
    driver.execute_script("arguments[0].click();", dropdown_entities)

    # Wait for dropdown to be fully visible
    entities = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[3]/div[1]/div/div/div[2]/ul')))

    # Get all entities items directly with a single call
    entities_items = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[3]/div[1]/div/div/div[2]/ul/li')))
    
    # ActionChains(driver).move_to_element(entities_items[1]).click().perform()
    print("Entities items found:", len(entities_items))
    # loop through the entities
    for i in range(len(entities_items)):
        if i == 0:
            continue
        # Re-fetch the entities list to avoid stale element issues
        entities_items = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[3]/div[1]/div/div/div[2]/ul/li'))
        )
        time.sleep(1)
        # Click on the entities
        print(f"Attempting to click: {entities_items[i].text}")
        ActionChains(driver).move_to_element(entities_items[i]).click().perform()

        # Reopen the dropdown to refresh the list
        dropdown_entities = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/section/div[2]/div[3]/div[1]/div/section/section[2]/div/div[3]/div[1]/div/button'))
        )
        driver.execute_script("arguments[0].click();", dropdown_entities)

    return dropdown_entities

# loop through the sectors
for i in range(len(sector_items)):
    if i == 0:
        continue
    # Click on the sector
    print(f"Attempting to click: {sector_items[i].text}")
    ActionChains(driver).move_to_element(sector_items[i]).click().perform()

    entities_scrape()
    
    #go back to dropmenu
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
