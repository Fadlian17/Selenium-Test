from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Automation\selenium-test\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.saucedemo.com/")
print(driver.title)

##Search
search = driver.find_element_by_id("user-name")
search.send_keys("standard_user")
search.send_keys(Keys.RETURN)
search_2 = driver.find_element_by_id("password")
search_2.send_keys("secret_sauce")
search_2.send_keys(Keys.RETURN)
button = driver.find_element_by_id("login-button")
button.click()

# try:
#     main = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID,"main"))
#     )

#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)
