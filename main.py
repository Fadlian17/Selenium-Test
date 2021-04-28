from selenium import webdriver

PATH = "C:\Automation\selenium-test\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)
driver.quit