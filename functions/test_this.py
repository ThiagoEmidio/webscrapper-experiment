from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from functions.save_page_source import save_page_source
from functions.wait_for_all_elements import wait_for_all_elements

def test_this(driver:WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    wait_for_all_elements(driver,2)
    emailElement = driver.find_element(By.ID, "username")
    passwordElement = driver.find_element(By.ID, "password")
    submitbutton = driver.find_element(By.ID,"submit")
    emailElement.send_keys("student")
    passwordElement.send_keys("Password123")
    wait_for_all_elements(driver,2)
    submitbutton.click()
    wait_for_all_elements(driver,2)
    save_page_source(driver)
    print(driver.current_url)
