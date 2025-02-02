import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    #def __init__(self):
    driver = None
    def test_e2e(self):

        self.driver.implicitly_wait(4)  # implicit wait
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # //a[contains(@href,'shop')]

        products = self.driver.find_elements(By.XPATH, "//app-card")

        for product in products:
            productName = product.find_element(By.XPATH, "div/div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/div/button").click()

        self.driver.find_element(By.XPATH, "//div/ul/li/a").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successtext

        time.sleep(2)