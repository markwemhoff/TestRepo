import unittest
import softest
import pytest
import time
import base
from utils import Utils
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestHudlLoginLinks(softest.TestCase):
    log = Utils.custom_logger()
    
    #Locators
    mainPageTitle = "Hudl • Tools to help every team, coach and athlete improve"
    loginPageTitle = "Log In"
    loginButton = "/html/body/div[1]/header/div/div/a"
    hudlButton = "/html/body/div[1]/header/div/div/div/div/div[1]/div/a/span"
    createAccountButton = "nav-btn-page"
    createAccountTitle = "Sign up for Hudl"
    createAccountText = "Request a Free Demo"
    createAccountLocation = '//*[@id="s_133036-r_1-c_1-copy"]/div/h1'
    forgotButton = "forgot-password"
    forgotTitle = "Log In"
    forgotText = "Let’s reset your password"
    forgotLocation = '//*[@id="app"]/section/div[2]/div/form/div/h3[1]'
    backButton = '//*[@id="app"]/section/a/span'

    def test_create_link(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)
        self.driver.find_element(By.ID, self.createAccountButton).click()
        time.sleep(1)
        self.log.info("|"+self.createAccountTitle+"|")
        self.log.info("|"+self.driver.title+"|")
        self.soft_assert(self.assertEqual, self.createAccountTitle, self.driver.title)

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.createAccountLocation), self.createAccountText))
        except:
            self.driver.save_screenshot(self.createAccountText+".png")
            raise NoSuchElementException("Could not find "+createAccountText+".")
 
        self.assert_all()

    def test_forgot_link(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)
        self.driver.find_element(By.ID, self.forgotButton).click()
        time.sleep(1)
        self.log.info("|"+self.forgotTitle+"|")
        self.log.info("|"+self.driver.title+"|")
        self.soft_assert(self.assertEqual, self.forgotTitle, self.driver.title)

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.forgotLocation), self.forgotText))
        except:
            self.driver.save_screenshot(self.forgotText+".png")
            raise NoSuchElementException("Could not find "+forgotText+".")
            
        self.driver.find_element(By.XPATH, self.backButton).click()
 
        self.assert_all()
