from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
# driver.implicitly_wait(2)
driver.maximize_window()


searBox=driver.find_element_by_name("search_query")
searBox.send_keys( 'hello').click()
driver.find_element_by_id('search-icon-legacy').click()
