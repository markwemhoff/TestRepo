import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_until_id_is_clickable(driver, element, sleeper=15):
    wait = WebDriverWait(driver, sleeper)
    try:
        wait.until(EC.element_to_be_clickable((By.ID,element)))
        time.sleep(1)
    except:
        driver.save_screenshot(element+".png")
        raise NoSuchElementException("Could not find element in time.")
        
def wait_until_text_is_present(driver, bytype, element, textstring, sleeper=15):
    wait = WebDriverWait(driver, sleeper)
    
    try:
        wait.until(EC.text_to_be_present_in_element((bytype, element), textstring))
    except:
        driver.save_screenshot(element+".png")
        raise NoSuchElementException("Could not find "+textstring+".")
