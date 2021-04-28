from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Automation\selenium-test\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

#Navigation
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.clear()
    element.click()

    # element = WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.ID,"menu-item-25"))
    # )
    # element.click()

    #All
    driver.back()
    driver.forward()

except:
    driver.quit()

finally:
    driver.quit()