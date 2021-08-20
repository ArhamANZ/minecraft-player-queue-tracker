from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://api.hypixel.net/player?key=e1fe1b8e-0a39-48ee-a9c9-be06ea8ff8b7&uuid=d6%27)
#page = driver.find_element_by_xpath('/html/body')
time.sleep(1)
for i in range(3):
    updates = driver.find_elements_by_xpath("/html/body")
    driver.refresh()
    if updates == updates :
        print("No change")
    else :
        print("Change")
    time.sleep(1)