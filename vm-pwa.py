from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class WebTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def testHomePage(self):
    #     self.driver.get("http://192.168.7.122:8080/menu")

    def testBuyCard(self):
        self.driver.get("http://192.168.7.122:8080/menu")
        self.driver.set_window_size(967, 736)
        self.driver.find_element(By.CSS_SELECTOR, ".v-card > .v-image > .v-responsive__content").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) .v-responsive__sizer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated > .v-btn__content").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1) .v-responsive__content").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
        self.driver.close()
  

    def testTopup(self):
        self.driver.get("http://192.168.7.122:8080/menu")
    #     self.driver.find_element_by_name("q").send_keys("Fadli")
    #     self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



if __name__ ==  '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Automation/selenium-test/reports'))