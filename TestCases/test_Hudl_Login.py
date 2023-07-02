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
class TestHudlLogin(softest.TestCase):
    log = Utils.custom_logger()
    
    #Locators
    mainPageTitle = "Hudl • Tools to help every team, coach and athlete improve"
    loginPageTitle = "Log In"
    homeTitlePage = "Log In"
    homeTitlePage2 = "Submit This Form"
    loginButton = "/html/body/div[1]/header/div/div/a"
    hudlButton = "/html/body/div[1]/header/div/div/div/div/div[1]/div/a/span"
    homeTeam = "Newcastle Jets FC"
    homeTeamLocation = '//*[@id="ssr-webnav"]/div/div[1]/nav[2]/div[2]/a/div[2]/span'
    fullName = "Mark W"
    fullNameLocation = '//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]/span'
    logoutButton = '//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a/span'
    continueButton = "logIn"

    @file_data("../TestData/testdata.json")
    def test_good_login(self, usernamestr, passwordstr):
        wait = WebDriverWait(self.driver, 15)
        self.log.info(self.mainPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.mainPageTitle, self.driver.title)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)

        UserName = self.driver.find_element(By.ID, "email")
        UserName.send_keys(usernamestr)
        UserName.send_keys(Keys.TAB)
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys(passwordstr)
        Password.send_keys(Keys.RETURN)
        time.sleep(1)
        self.log.info(self.homeTitlePage)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.homeTitlePage, self.driver.title)

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.homeTeamLocation), self.homeTeam))
        except:
            self.driver.save_screenshot(self.homeTeam+".png")
            raise NoSuchElementException("Could not find "+homeTeam+".")

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.fullNameLocation), self.fullName))
        except:
            self.driver.save_screenshot(self.fullName+".png")
            raise NoSuchElementException("Could not find "+fullName+".")

        UserMenu = self.driver.find_element(By.XPATH, self.fullNameLocation)    
        Hover = ActionChains(self.driver).move_to_element(UserMenu)
        Hover.perform()
        self.driver.find_element(By.XPATH, self.logoutButton).click()
        time.sleep(1)
        self.log.info(self.mainPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.mainPageTitle, self.driver.title) 
        self.assert_all()
        
    @file_data("../TestData/testdata.json")
    def test_good_login_continue(self, usernamestr, passwordstr):
        wait = WebDriverWait(self.driver, 15)
        self.log.info(self.mainPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.mainPageTitle, self.driver.title)
        self.driver.find_element(By.XPATH, self.loginButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.hudlButton).click()
        time.sleep(1)
        self.log.info(self.loginPageTitle)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.loginPageTitle, self.driver.title)

        UserName = self.driver.find_element(By.ID, "email")
        UserName.send_keys(usernamestr)
        UserName.send_keys(Keys.TAB)
        Password = self.driver.find_element(By.ID, "password")
        Password.send_keys(passwordstr)
        self.driver.find_element(By.ID, self.continueButton).click()
        time.sleep(1)
        self.log.info(self.homeTitlePage2)
        self.log.info(self.driver.title)
        self.soft_assert(self.assertEqual, self.homeTitlePage2, self.driver.title)

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.homeTeamLocation), self.homeTeam))
        except:
            self.driver.save_screenshot(self.homeTeam+".png")
            raise NoSuchElementException("Could not find "+homeTeam+".")

        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, self.fullNameLocation), self.fullName))
        except:
            self.driver.save_screenshot(self.fullName+".png")
            raise NoSuchElementException("Could not find "+fullName+".")

        UserMenu = self.driver.find_element(By.XPATH, self.fullNameLocation)    
        Hover = ActionChains(self.driver).move_to_element(UserMenu)
        Hover.perform()
        self.driver.find_element(By.XPATH, self.logoutButton).click()
        time.sleep(1)
        self.log.warning(self.mainPageTitle)
        self.log.warning(self.driver.title)
        self.soft_assert(self.assertEqual, self.mainPageTitle, self.driver.title) 
        self.assert_all()
