""" The Purpose of this script is to download IMD data automatically for all the available years
Developed by Rajasirpi S
Date: 21-06-2021"""
# -*- coding: utf-8 -*-
from selenium import webdriver     # Importing the required modules 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
        "download.default_directory": "D:IMD\data"})
        self.driver = webdriver.Chrome(options=options)     # setting the download directory location through chrome options.
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.imdpune.gov.in/Clim_Pred_LRF_New/Grided_Data_Download.html")  # the link from where data are going to be downloaded.
        for x in range(1901,2021):                                                            # looping by giving start years and end years for which data are needed.             
            driver.find_element_by_id("rain").click()           
            Select(driver.find_element_by_id("rain")).select_by_visible_text("%s"%(x))        # finding the elements by id tag and downloading it.
            # Select(driver.find_element_by_id("rain")).select_by_visible_text("2020")
            driver.find_element_by_id("rain").click()
            driver.find_element_by_xpath("//input[@value='Download']").click()
            time.sleep(10)                                                                    # Similarly repteated the process for all 5 types of data
        for x in range(1951,2021):
            driver.find_element_by_id("RF25").click()
            Select(driver.find_element_by_id("RF25")).select_by_visible_text("%s"%(x))
            driver.find_element_by_id("RF25").click()
            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form[2]/input").click()
            time.sleep(10)
        for x in range(1901,2020):  
            driver.find_element_by_id("rainone").click()
            Select(driver.find_element_by_id("rainone")).select_by_visible_text("%s"%(x))
            driver.find_element_by_id("rainone").click()
            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form[3]/input").click()
            time.sleep(5)
        for x in range(1951,2021):  
            driver.find_element_by_id("maxtemp").click()
            Select(driver.find_element_by_id("maxtemp")).select_by_visible_text("%s"%(x))
            driver.find_element_by_id("maxtemp").click()
            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form[4]/input").click()
            time.sleep(5)
        for x in range(1951,2021):
            driver.find_element_by_id("mintemp").click()
            Select(driver.find_element_by_id("mintemp")).select_by_visible_text("%s"%(x))
            driver.find_element_by_id("mintemp").click()
            driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form[5]/input").click()
            time.sleep(5)
      
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


