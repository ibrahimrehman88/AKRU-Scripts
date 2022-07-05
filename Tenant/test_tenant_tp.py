# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from chrome_setup import chrome


class TestTenant():
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    #self.vars = {}

    csk = chrome()
    self.driver = csk.get_driver()
    driverl = self.driver
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tenant(self):
    self.driver.get("https://avaxdevtenants.akru.co/")
    self.driver.set_window_size(1200, 668)
    self.driver.find_element(By.ID, "navbar-header-sticky-login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiPaper-root > button").click()
    self.driver.find_element(By.ID, "navbar-select-magic").click()
    self.driver.find_element(By.ID, "navbar-magic-email").click()
    self.driver.find_element(By.ID, "navbar-magic-email").send_keys("tenantav3@yopmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,52)")
  