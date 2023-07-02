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
class TestHudlLoginFail(softest.TestCase):
    log = Utils.custom_logger()
    
    #Locators
    loginPageTitle = "Log In"
    loginButton = "/html/body/div[1]/header/div/div/a"
    hudlButton = "/html/body/div[1]/header/div/div/div/div/div[1]/div/a/span"
    loginErrorLocation = "login-box"
    loginError = "object Object"
    homeButton = "nav-btn-logo-hudl"
    continueButton = "logIn"
    requiredError = "Please fill in all of the required fields."

    def test_bad_login(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)

        UserName = self.driver.find_element(By.ID, "email")
        UserName.send_keys("baduser")
        UserName.send_keys(Keys.TAB)
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys("badpass")
        Password.send_keys(Keys.RETURN)
        time.sleep(1)
        
        try:
            wait.until(EC.text_to_be_present_in_element((By.ID, self.loginErrorLocation), self.loginError))
        except:
            self.driver.save_screenshot(self.loginError+".png")
            raise NoSuchElementException("Could not find "+loginError+".")
            
        self.driver.find_element(By.ID, self.homeButton).click()

        self.assert_all()

    def test_blank_login(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)
        self.driver.find_element(By.ID, self.continueButton).click()
        time.sleep(1)
        
        try:
            wait.until(EC.text_to_be_present_in_element((By.ID, self.loginErrorLocation), self.requiredError))
        except:
            self.driver.save_screenshot(self.requiredError+".png")
            raise NoSuchElementException("Could not find "+requiredError+".")
            
        self.driver.find_element(By.ID, self.homeButton).click()

        self.assert_all()

    def test_blank_email(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys("badpass")
        self.driver.find_element(By.ID, self.continueButton).click()
        time.sleep(1)
        
        try:
            wait.until(EC.text_to_be_present_in_element((By.ID, self.loginErrorLocation), self.requiredError))
        except:
            self.driver.save_screenshot(self.requiredError+".png")
            raise NoSuchElementException("Could not find "+requiredError+".")
            
        self.driver.find_element(By.ID, self.homeButton).click()

        self.assert_all()

    def test_blank_password(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)
        UserName = self.driver.find_element(By.ID, "email")
        UserName.send_keys("baduser")
        self.driver.find_element(By.ID, self.continueButton).click()
        time.sleep(1)
        
        try:
            wait.until(EC.text_to_be_present_in_element((By.ID, self.loginErrorLocation), self.requiredError))
        except:
            self.driver.save_screenshot(self.requiredError+".png")
            raise NoSuchElementException("Could not find "+requiredError+".")
            
        self.driver.find_element(By.ID, self.homeButton).click()

        self.assert_all()