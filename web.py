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
button2 = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
button2.click()
button3 = driver.find_element_by_id("shopping_cart_container")
button3.click()
buttonCheck = driver.find_element_by_id("checkout")
buttonCheck.click()


#Checkout
# checkout = driver.find_element_by_id("first-name")
# checkout.send_keys("fadli")
# checkout.send_keys(Keys.RETURN)
# checkout_2 = driver.find_element_by_id("last-name")
# checkout_2.send_keys("alfa")
# checkout_2.send_keys(Keys.RETURN)
# checkout_3 = driver.find_element_by_id("postal-code")
# checkout_3.send_keys("13370")
# checkout_3.send_keys(Keys.RETURN)
# buttonContinue = driver.find_element_by_id("continue")
# buttonContinue.click()
# try:
#     main = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID,"main"))
#     )

#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)
