from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://api.hypixel.net/player?key=996a0ea0-ad8a-460d-9e19-a5bb9623acb6&uuid=d62192a9-a142-42dd-bc81-b400843430f0')
#searchbox = driver.find_element_by_xpath('//*[@id="search"]')
#searchbox.send_keys('Bad girls')

#searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#searchButton.click()